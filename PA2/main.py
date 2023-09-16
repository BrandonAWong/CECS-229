import random
import math
import pa2
import alt_sol

        

print("Welcome to the PA #2 Tester")

while True:
  user_in = input(
    "\n" + "-" * 50 +
    "\nWhich problem would you like to test?\n1.  Problem 1: primes(a, b)\n2.  Problem 2: bezout_coeffs(a, b)\n3.  Problem 3: gcd(a, b)\n4.  Quit\n\nEnter your selection: "
  )
  if user_in == '1':
    print( "\n" + "-" * 50 + "\n\nTesting Problem 1...\n\n")
    a = random.randint(1, 60)
    b = random.randint(a+15, 100)
    expected = alt_sol.primes(a, b)
    received = pa2.primes(a, b)

    print(f"Testing primes({a}, {b})....\nExpected: {expected}\nReceived: {received}")

    if expected == received:
      print("\nTest PASSED!")
    else:
      print("\nTest FAILED.")

  elif user_in == '2':
    print( "\n" + "-" * 50 + "\n\nTesting Problem 2...\n\n")
    a = random.randint(1, 60)
    b = random.randint(a+15, 100)
    expected = alt_sol.bezout_coeffs(a, b)
    received = pa2.bezout_coeffs(a, b)

    print(f"Testing bezout_coeffs({a}, {b})....\nExpected: {expected}\nReceived: {received}")

    if expected == received:
      print("\nTest PASSED!")
    else:
      print("\nTest FAILED.")

  elif user_in == '3':
    print( "\n" + "-" * 50 + "\n\nTesting Problem 3...\n\n")

    a = random.randint(-100, 100)
    while a == 0:
      a = random.randint(-100, 100)
    expected = math.gcd(a, a)
    received = pa2.gcd(a, a)

    print(f"Testing gcd({a}, {a})....\n\tExpected: {expected}\n\tReceived: {received}") 
    
    if expected == received:
      print("\tTest PASSED!\n")
    else:
      print("\tTest FAILED.\n")
    
    possibilities = [-1, 1]
    for i in possibilities:
      for j in possibilities:
        if i < 0:
          a = random.randint(-100, -50)
          while a == 0:
            a = random.randint(-100, 100)
        else:
          a = random.randint(50, 100)
          while a == 0:
            a = random.randint(-100, 100)
        if j < 0:
          b = random.randint(-100, -50)
          while b == 0:
            b = random.randint(-100, 100)
        else:
          b = random.randint(-100, -50)
          while b == 0:
            b = random.randint(-100, 100)

        expected = math.gcd(a, b)
        received = pa2.gcd(a, b)

        print(f"Testing gcd({a}, {b})....\n\tExpected: {expected}\n\tReceived: {received}")  

        if expected == received:
          print("\tTest PASSED!\n")
        else:
          print("\tTest FAILED.\n")


  elif user_in == '4' or user_in.upper() == 'Q':
    break
  else:
    print("Invalid selection.  Please try again.")
