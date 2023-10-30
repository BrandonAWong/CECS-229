import pa5
from vec import Vec
import numpy as np
from random import randint
from random import random

def initialize_matrices(m, n):
  rowsp = [[randint(-10, 10) for j in range(n)] for i in range(m)]
  matrix = pa5.Matrix(rowsp)
  expected_rowsp = np.array(rowsp)
  return [expected_rowsp, matrix]

print("Welcome to the PA #5 Tester")

while True:

  user_in = input(
      "\n" + "-" * 50 +
      "\nWhat would you like to test?\n1.  Matrix constructor\n2.  Matrix getter methods\n3.  Matrix setter methods\n4.  Matrix operators\nQ.  Quit\n\nEnter your selection: "
  )
  if user_in == '1':
    print("\n" + "-" * 50 + "\n\nTesting Matrix constructor...\n")
    m = randint(2, 5)
    n = randint(2, 5)
    print(f"Creating Matrix object with {m} rows and {n} columns...")
    expected_rowsp, matrix = initialize_matrices(m, n)
    expected_colsp = expected_rowsp.transpose()

    print("\nExpected row space:\n", expected_rowsp)
    print("\nReturned Matrix row space:\n[", end="")
    for row in matrix.rowsp:
      print(row)
    print(']')

    print("\n\nExpected column space:\n", expected_colsp)
    print("\nReturned Matrix column space:\n[", end="")
    for col in matrix.colsp:
      print(col)
    print(']')


    if np.array_equal(matrix.rowsp,
                      np.array(expected_rowsp)) and np.array_equal(
                          matrix.colsp, np.array(expected_colsp)):
      print("\nTest Passed!")
    else:
      print("\nTest Failed!")

  # ---------------- OPTION 2 ------------------ #
  elif user_in == '2':
    print("\n" + "-" * 50 + "\n\nTesting Matrix getter methods...\n")
    m = randint(2, 5)
    n = randint(2, 5)
    print(f"Creating Matrix object with {m} rows and {n} columns...")
    expected_rowsp, matrix = initialize_matrices(m, n)
    expected_colsp = expected_rowsp.transpose()
    print(expected_rowsp)

    # getting row
    i = randint(1, m) 
    print(f"\nTesting matrix.get_row({i})")
    returned_row = matrix.get_row(i)
    expected_row = expected_rowsp[i-1]
    print(f"\tExpected: {list(expected_row)}\n\tReturned: {returned_row}")
    if np.array_equal(np.array(returned_row), expected_row):
      print("\tTest Passed!")
    else:
      print("\tTest Failed!")

    # getting column
    j = randint(1, n)
    print(f"\nTesting matrix.get_col({j})")
    returned_col = matrix.get_col(j)
    expected_col = expected_colsp[j-1]
    print(f"\tExpected: {list(expected_col)}\n\tReturned: {returned_col}")
    if np.array_equal(np.array(returned_col), expected_col):
      print("\tTest Passed!")
    else:
      print("\tTest Failed!")

    # getting entry
    i = randint(1, m) 
    j = randint(1, n) 
    print(f"\nTesting matrix.get_entry({i}, {j})")
    returned_ele = matrix.get_entry(i, j)
    expected_ele = expected_rowsp[i-1][j-1]
    print(f"\tExpected: {expected_ele}\n\tReturned: {returned_ele}")
    if returned_ele == expected_ele:
      print("\tTest Passed!")
    else:
      print("\tTest Failed!")

    # getting row space
    print("\nTesting matrix.row_space()")
    returned_rows = matrix.row_space()
    print(f"\tExpected:\n\t{expected_rowsp}\n\tReturned:\n\t{returned_rows}")
    if np.array_equal(np.array(returned_rows), expected_rowsp):
      print("\tTest Passed!")
    else:
      print("\tTest Failed!")

    # getting col space
    print("\nTesting matrix.col_space()")
    returned_cols = matrix.col_space()
    print(f"\tExpected:\n\t{expected_colsp}\n\tReturned:\n\t{returned_cols}")
    if np.array_equal(np.array(returned_cols), expected_colsp):
      print("\tTest Passed!")
    else:
      print("\tTest Failed!")


    # getting diag

    for d in range(n):
      print(f"\nTesting matrix.get_diag({d})")
      expected_diag = np.diag(expected_rowsp, k=d)
      returned_diag = matrix.get_diag(d)
      print(f"\tExpected:\n\t{expected_diag}\n\tReturned:\n\t{returned_diag}")
      if np.array_equal(np.array(returned_diag), expected_diag):
        print("\tTest Passed!")
      else:
        print("\tTest Failed!")

    for d in reversed(range(-1*m + 1, 0)):
      print(f"\nTesting matrix.get_diag({d})")
      expected_diag = np.diag(expected_rowsp, k=d)
      returned_diag = matrix.get_diag(d)
      print(f"\tExpected:\n\t{list(expected_diag)}\n\tReturned:\n\t{returned_diag}")
      if np.array_equal(np.array(returned_diag), expected_diag):
        print("\tTest Passed!")
      else:
        print("\tTest Failed!")  

  # ---------------- OPTION 3 ------------------ #
  elif user_in == '3':
    print("\n" + "-" * 50 + "\n\nTesting Matrix setter methods...\n")
    m = randint(2, 5)
    n = randint(2, 5)
    print(f"Creating Matrix object with {m} rows and {n} columns...")
    expected_rowsp, matrix = initialize_matrices(m, n)
    print(expected_rowsp)

    new_row = [randint(-10, 10) for i in range(n)]
    i = randint(1, m)
    print(f"\nTesting matrix.set_row({i}, {new_row})")

    matrix.set_row(i, new_row)
    expected_rowsp[i-1] = new_row
    expected_colsp = expected_rowsp.transpose()
    print(f"Expected matrix:\n{expected_rowsp}\n\nReturned matrix:\n{matrix}")
    print(f"\nExpected row space: {expected_rowsp.tolist()}\nReturned row space: {matrix.rowsp}")
    print(f"\nExpected col space: {expected_colsp.tolist()}\nReturned col space: {matrix.colsp}")

    if np.array_equal(np.array(matrix.rowsp), expected_rowsp) and np.array_equal(np.array(matrix.colsp), expected_colsp):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    new_col = [randint(-10, 10) for i in range(m)]
    j = randint(1, n)
    print(f"\n\nTesting matrix.set_col({j}, {new_col})")

    matrix.set_col(j, new_col)

    expected_colsp[j-1] = new_col
    expected_rowsp = expected_colsp.transpose()
    print(f"Expected matrix:\n{expected_rowsp}\n\nReturned matrix:\n{matrix}")

    print(f"\nExpected row space: {expected_rowsp.tolist()}\nReturned row space: {matrix.rowsp}")
    print(f"\nExpected col space: {expected_colsp.tolist()}\nReturned col space: {matrix.colsp}")

    if np.array_equal(np.array(matrix.rowsp), expected_rowsp) and np.array_equal(np.array(matrix.colsp), expected_colsp):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    new_ele = randint(-10, 10)
    i = randint(1, m)
    j = randint(1, n)
    print(f"\n\nTesting matrix.set_entry({i}, {j}, {new_ele})")

    matrix.set_entry(i, j, new_ele)

    expected_rowsp[i-1][j-1] = new_ele
    expected_colsp[j-1][i-1] = new_ele
    print(f"Expected matrix:\n{expected_rowsp}\n\nReturned matrix:\n{matrix}")

    print(f"\nExpected row space: {expected_rowsp.tolist()}\nReturned row space: {matrix.rowsp}")
    print(f"\nExpected col space: {expected_colsp.tolist()}\nReturned col space: {matrix.colsp}")

    if np.array_equal(np.array(matrix.rowsp), expected_rowsp) and np.array_equal(np.array(matrix.colsp), expected_colsp):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

  # ---------------- OPTION 4 ------------------ #
  elif user_in == '4':
    print("\n" + "-" * 50 + "\n\nTesting Matrix operators...\n")
    m = randint(2, 5)
    n = randint(2, 5)
    k = randint(2, 5)
    while n == k:
      k = randint(2, 5)
    print(f"Creating Matrix object with {m} rows and {n} columns...")
    exp_A, mat_A = initialize_matrices(m, n)
    print("A = \n", exp_A)

    print(f"\nCreating Matrix object with {m} rows and {n} columns...")
    exp_B, mat_B = initialize_matrices(m, n)
    print("B = \n", exp_B)

    print(f"\nCreating Matrix object with {n} rows and {k} columns...")
    exp_C, mat_C = initialize_matrices(n, k)
    print("C = \n", exp_C)

    print(f"\nCreating Vec object with {k} elements...")
    vec_k = Vec([randint(-10, 10) for i in range(k)])
    print("v =", vec_k)

    alpha = randint(-10, 10) + round(random(), 1)
    print(f"\nCreated scalar alpha = {alpha}")

    beta = randint(-10, 10)
    print(f"\nCreated scalar beta = {beta}")

    print('-'*20)
    print(f"\nTesting A+B:")
    expected = exp_A + exp_B
    result = mat_A + mat_B
    print(f"\nExpected:\n{expected}\n\nReturned:\n{result}")
    if np.array_equal(np.array(result.rowsp), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    print('-'*20)
    print(f"\nTesting A-B:")
    expected = exp_A - exp_B
    result = mat_A - mat_B
    print(f"\nExpected:\n{expected}\n\nReturned:\n{result}")
    if np.array_equal(np.array(result.rowsp), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")
    print('-'*20)
    print(f"\nTesting {alpha} * A:")
    expected = alpha * exp_A
    result = alpha * mat_A
    print(f"\nExpected:\n{expected}\n\nReturned:\n{result}")
    if np.array_equal(np.array(result.rowsp), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    print('-'*20)
    print(f"\nTesting {beta} * A:")
    expected = beta * exp_A
    result = beta * mat_A
    print(f"\nExpected:\n{expected}\n\nReturned:\n{result}")
    if np.array_equal(np.array(result.rowsp), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    print('-'*20)
    print(f"\nTesting A * {alpha}:")
    expected = alpha * exp_A
    result = mat_A * alpha
    print(f"\nExpected:\n{expected}\n\nReturned:\n{result}")
    if np.array_equal(np.array(result.rowsp), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    print('-'*20)
    print(f"\nTesting A * {beta}:")
    expected = exp_A * beta
    result = mat_A * beta
    print(f"\nExpected:\n{expected}\n\nReturned:\n{result}")
    if np.array_equal(np.array(result.rowsp), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    print('-'*20)
    print(f"\nTesting C * {vec_k}:")
    vec = np.array(vec_k.elements).transpose()
    expected = np.dot(exp_C , np.array(vec_k.elements))

    result = mat_C * vec_k
    print(f"\nExpected: {expected}\n\nReturned: {result}")
    if np.array_equal(np.array(result.elements), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    print('-'*20)
    print(f"\nTesting B * C:")

    expected = np.dot(exp_B , exp_C)
    result = mat_B * mat_C
    print(f"\nExpected:\n{expected}\n\nReturned:\n{result}")
    if np.array_equal(np.array(result.rowsp), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

  # ---------------- OPTION Q ------------------ #
  if user_in.upper() == 'Q':
    print("\n" + "-" * 50 + "\n\nGoodbye!")
    break
