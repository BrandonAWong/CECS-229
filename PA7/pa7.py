from helpers import gram_schmidt
from structures import Vec, Matrix
import numpy as np
import cmath


# ----------------------- PROBLEM 1 ----------------------- #
def qr_solve(A: Matrix, b: Vec):
  """
    Solves the system of equations Ax = b by using the
    QR factorization of Matrix A
    :param A: Matrix of coefficients of the system
    :param b: Vec of constants
    :return:  Vec solution to the system
    """
  # Constructing U
  # U should be the set of orthonormal vectors returned
  # by applying Gram-Schmidt Process to the columns of A
  U = gram_schmidt([Vec(c) for c in A.col_space()])
  n = len(U)

  # Constructing Q
  # Q should be the matrix whose columns are the elements
  # of the vector in set U
  Q = Matrix([[None for j in range(n)] for i in range(n)])
  for j in range(n):
    [Q.set_entry(i+1, j+1, U[j][i]) for i in range(n)]

  # Constructing R
  R = Matrix([[0 for j in range(n)] for i in range(n)])
  for j in range(n):
    for i in range(n):
      if i <= j:
        R.set_entry(i+1, j+1, sum(U[i][k] * A.get_entry(k+1, j+1) for k in range(n)))

  # Constructing the solution vector x
  b_star = Q.transpose() * b
  x = [None for i in range(n)]
  for i in reversed(range(n)):
    x[i] = b_star[i]
    for j in range(i + 1, n):
        x[i] -= R.get_entry(i + 1, j + 1) * x[j]
    x[i] /= R.get_entry(i + 1, i + 1)
  return Vec(x)


# ----------------------- PROBLEM 2 ----------------------- #
def _submatrix(A: Matrix, i: int, j: int):
  """
    constructs the sub-matrix of an mxn Matrix A that
    results from omitting the i-th row and j-th column;
    i and j satisfy that 0 <= i <= m, and 0 <= j <= n
    :param A: Matrix object
    :param i: int index of row to omit
    :param j: int index of column to omit
    :return: Matrix object representing the sub-matrix
    """
  m, n = A.dim()
  return Matrix([[col for jc, col in enumerate(row) if jc != j-1] for ir, row in enumerate(A.row_space()) if ir != i-1])


# ----------------------- PROBLEM 3 ----------------------- #
def determinant(A: Matrix):
  """
    computes the determinant of square Matrix A;
    Raises ValueError if A is not a square matrix.
    :param A: Matrix object
    :return: float value of determinant
    """
  m, n = A.dim()
  if m != n:
    raise ValueError(
        f"Determinant is not defined for Matrix with dimension {m}x{n}.  Matrix must be square."
    )
  if n == 1:
    return A.get_entry(1, 1)
  elif n == 2:
    return A.get_entry(1, 1) * A.get_entry(2, 2) - A.get_entry(1, 2) * A.get_entry(2, 1)
  else:
    d = 0
    for i in range(1, n+1):
      sm = _submatrix(A, 1, i)
      d += (-1) ** (1+i) * A.get_entry(1, i) * determinant(sm)
    return d


# ----------------------- PROBLEM 4 ----------------------- #
def eigen_wrapper(A: Matrix):
  """
    uses numpy.linalg.eig() to create a dictionary with
    eigenvalues of Matrix A as keys, and their corresponding
    list of eigenvectors as values.
    :param A: Matrix object
    :return: Python dictionary
    """
  evals, evecs = np.linalg.eig(A.row_space())
  edic = {}
  for i in range(len(evals)):
    edic[evals[i]] = evecs[:,i].tolist()
  return {v: Vec(edic[v]) for v in edic}



# ----------------------- PROBLEM 5 ----------------------- #
def svd(A: Matrix):
  """
    computes the singular value decomposition of Matrix A;
    returns Matrix objects U, Sigma, and V such that
        1. V is the Matrix whose columns are eigenvectors of 
        A.transpose() * A
        2. Sigma is a diagonal Matrix of singular values of 
        A.transpose() * A appearing in descending order along 
        the main diagonal
        3. U is the Matrix whose j-th column uj satisfies 
        A * vj = sigma_j * uj where sigma_j is the j-th singular value in 
        decreasing order and vj is the j-th column vector of V
        4. A = U * Sigma * V.transpose()
    :param A: Matrix object
    :return: tuple with Matrix objects; (U, Sigma, V)
    """
  m, n = A.dim()
  aTa = A.transpose() * A
  eigen = eigen_wrapper(aTa)
  eigenvalues = np.sort_complex(list(eigen.keys())).tolist()[::-1]

  # Constructing V
  # V should be the mxm matrix whose columns
  # are the eigenvectors of matrix A.transpose() * A
  V = Matrix([[None for j in range(n)] for i in range(n)])
  for j in range(1, n + 1):
    eigenvector = eigen[eigenvalues[j - 1]]
    for i in range(n):
        V.set_entry(i + 1, j, eigenvector[i])

  # Constructing Sigma
  # Sigma should be the mxn matrix of singular values.
  singular_values = [np.sqrt(np.abs(ev)) for ev in eigenvalues]
  #        holds a list of singular values of A
  #        in decreasing order
  Sigma = Matrix([[0 for j in range(n)] for i in range(m)])
  for i in range(1, m + 1):
    if m > n and i > n:
      break
    Sigma.set_entry(i, i, singular_values[i - 1])

  # Constructing U
  # U should be the matrix whose j-th column is given by
  # A * vj / sj where vj is the j-th eigenvector of A.transpose() * A
  # and sj is the corresponding j-th singular value
  U = Matrix([[None for j in range(m)] for i in range(m)])
  for j in range(1, m + 1):
    if m > n and j > n:
      break

    vj = Vec([V.get_entry(i, j) for i in range(1, n + 1)])
    sj = singular_values[j - 1]
    if sj != 0:
      uj = (A * vj) / float(sj)
      for i in range(m):
        U.set_entry(i + 1, j, uj[i])
    else:
      for i in range(m):
          U.set_entry(i + 1, j, 0)
  U = Matrix([[c if c else 0 for c in r] for r in U.row_space()])
  return (U, Sigma, V)
