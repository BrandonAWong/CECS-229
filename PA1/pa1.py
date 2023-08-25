""" ---------------- PROBLEM 1 ----------------"""
def equiv_to(a, m, low, high):
    return [num for num in list(range(low, high+1)) if (num - a) % m == 0]
    

""" ---------------- PROBLEM 2 ----------------"""
def b_expansion(n, b):
    digits = [] # stores the digits of the b-expansion
    q = n
    while q != 0:
        digit = q % b
        if b == 16 and digit > 9:
            hex_dict = {10: 'A', 11 : 'B', 12: 'C', 13: 'D', 14: 'E', 15 : 'F'}
            digit = hex_dict.get(digit)
        digits.append(str(digit))
        q //= b
    return "".join(reversed(digits))
        

""" ---------------- PROBLEM 3 ----------------"""
def binary_add(a, b): 
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')
    
    # padding the strings with 0's so they are the same length
    if len(a) < len(b):
        diff = len(b) - len(a)
        a = "0" *diff + a
    elif len(a) > len(b):
        diff = len(a) - len(b)
        b = "0" *diff + b
    
    # addition algorithm
    result = ""
    carry = 0
    for i in reversed(range(len(a))):
        a_i = int(a[i])
        b_i = int(b[i])
    
        result += '1' if a_i + b_i + carry == 1 or a_i + b_i + carry == 3 else '0'
        carry = 1 if a_i + b_i + carry >= 2 else 0
    if carry == 1:
        result += '1'
    return "".join(reversed(result))

""" ---------------- PROBLEM 4 ----------------"""
def binary_mul(a, b):
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')
    
    # multiplication algorithm
    partial_products = []
    i = 0 # index of the current binary bit of string 'a' beginning at 0, right-to-left
    for bit in reversed(a):
        if bit == '1':
          partial_products.append(f"{b}{'0'*i}")
        i += 1

    result = '0'
    while len(partial_products) > 0:
        result = binary_add(result, partial_products[0])
        del partial_products[0]
    return result