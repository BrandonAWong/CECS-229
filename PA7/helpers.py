import copy
from structures import Matrix, Vec


def norm(v: Vec, p: int):
  """
  returns the p-norm of Vec v
  INPUT:
      p - an integer determining the norm to be calculated
      v - the Vec object for which the norm will be applied
  OUTPUT:
      the norm as a float
  """
  return sum(abs(v.elements[i])**p for i in range(len(v.elements)))**(1 / p)


def is_independent(S):
  rows = [vec.elements for vec in S]
  A = Matrix(rows)
  return rank(A) == len(S)


def gram_schmidt(S):
  if not is_independent(S):
    raise ValueError("The vectors are not linearly independent")
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


def _ref(A: Matrix):
  """
    returns the Row Echelon Form of the Matrix A
    INPUT: Matrix A
    OUTPUT: distinct Matrix object that is the
            Row-Echelon Form of A
    """
  matrix = Matrix(copy.deepcopy(A.rowsp))
  m, n = matrix.dim()

  # Iterate through each column
  for j in range(min(m, n)):
      # Find the first non-zero element in or below the current row
      pivot_row = next((i for i in range(j, m) if matrix.rowsp[i][j] != 0), None)

      if pivot_row is not None:
          # Swap rows to move the pivot to the current row
          matrix.rowsp[j], matrix.rowsp[pivot_row] = matrix.rowsp[pivot_row], matrix.rowsp[j]

          # Make the pivot element 1
          pivot_value = matrix.rowsp[j][j]
          for k in range(j, n):
              matrix.rowsp[j][k] /= pivot_value

          # Eliminate other elements in the current column
          for i in range(j + 1, m):
              factor = matrix.rowsp[i][j]
              for k in range(j, n):
                  matrix.rowsp[i][k] -= factor * matrix.rowsp[j][k]

  return matrix


def rank(A: Matrix):
  """
  returns the rank of the given Matrix object
  as an integer
  """
  mat = _ref(A)
  rank = sum([1 for row in mat.rowsp if any(row)])
  return rank


def frobenius_norm(A: Matrix):
  f = 0
  m, n = A.dim()
  for i in range(m):
    for j in range(n):
      f += abs(A.get_entry(i+1, j+1))**2
  return f**0.5


count = {
    1: 'First',
    2: 'Second',
    3: 'Third',
    4: 'Fourth',
    5: 'Fifth',
    6: 'Sixth',
    7: 'Seventh',
    8: 'Eighth',
    9: 'Ninth',
    10: 'Tenth'
}