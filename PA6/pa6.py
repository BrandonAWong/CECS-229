import copy
from structures import Matrix, Vec
""" ----------------- PROBLEM 1 ----------------- """


def norm( v : Vec, p : int):
  """
  returns the p-norm of Vec v
  INPUT:
      p - an integer determining the norm to be calculated
      v - the Vec object for which the norm will be applied
  OUTPUT:
      the norm as a float
  """
  return sum((abs(e) ** p for e in v)) ** (1/p)


""" ----------------- PROBLEM 2 ----------------- """


def _ref(A : Matrix):
  """
    returns the Row Echelon Form of the Matrix A
    INPUT: Matrix A
    OUTPUT: distinct Matrix object that is the
            Row-Echelon Form of A
    """
  matrix = Matrix(copy.deepcopy(A.rowsp))
  m, n = matrix.dim()
  cc = 0
  for row in range(m):
    if cc >= n:
      break
    p = None
    for r in range(row, m):
      if matrix.rowsp[r][cc] != 0:
        p = r
        break
    if p is not None:
      matrix.rowsp[row], matrix.rowsp[p] = matrix.rowsp[p], matrix.rowsp[row]
      pivot_value = matrix.rowsp[row][cc]
      matrix.rowsp[row] = [entry / pivot_value for entry in matrix.rowsp[row]]
      for r in range(row + 1, m):
        factor = matrix.rowsp[r][cc]
        matrix.rowsp[r] = [entry - factor * matrix.rowsp[row][i] for i, entry in enumerate(matrix.rowsp[r])]
      cc += 1
  return matrix


""" ----------------- PROBLEM 3 ----------------- """


def rank(A : Matrix):
  """
  returns the rank of the given Matrix object
  as an integer
  """
  matrix = _ref(A)
  c = 0
  for i in range(len(matrix.rowsp)):
    matrix.set_row(i+1, [r if r > 0.1**8 else 0 for r in matrix.get_row(i+1)])
    if any(matrix.get_row(i+1)):
      c += 1
  return c


""" ----------------- PROBLEM 4 ----------------- """


def gauss_solve(A : Matrix, b : Vec):
  """
  returns the solution to the system Ax = b 
  if the system has a solution.  If the system
  does not have a solution, None is returned.
  If the system has infinitely-many solutions,
  the number of free variables as an 'int' is returned
  INPUT:
      A - a Matrix object
      b - a Vec object

  OUTPUT:
      Vec object if the system has a unique solution
      None if the system has no solution
      int if the system has infinitely-many solutions
  """
  r = []
  for i in range(A.dim()[0]):
    r.append(A.get_row(i+1) + [b.elements[i]])
  ag = Matrix(r)

  if rank(A) < rank(ag):
    return None
  elif rank(A) == rank(ag) == len(A.col_space()) - 1:
    return Vec()
  else:
    return len(A.col_space()) - rank(A)


""" ----------------- PROBLEM 5 ----------------- """


def gram_schmidt(S : set):
  """
  returns the orthonormal basis of given set S
  INPUT: S - a set of linearly independent 'Vec' objects
  OUTPUT: An orthonormal set of 'Vec' objects
  """
  r = []
  for s in S:
    for e in r:
        p = (e * s) / (e * e) * e if (e * e) != 0 else Vec([0] * len(e))
        s -= p
    n = abs(s)
    if n:
        s /= n
    r.append(s)
  return r