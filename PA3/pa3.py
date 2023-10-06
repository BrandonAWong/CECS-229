from util import * 

def bezout_coeffs(a, b):
    s0 = 1
    t0 = 0
    s1 = -1 * (b//a)
    t1 = 1
    
    temp = b
    bk = a
    ak = temp % a
    
    while ak != 0:
        temp_s = s1
        temp_t = t1

        # FIXME: Update s1 according to the formula for sk
        s1 = s0 - s1 * (bk // ak)
        
        # FIXME: Update t1 according to the formula for tk
        t1 = t0 - t1 * (bk // ak)
        
        s0 = temp_s
        t0 = temp_t
        temp = bk
        
        # FIXME: Update bk and ak
        bk = ak
        ak = temp % ak
        
    # FIXME: Replace each string with the correct coefficients of a and b
    return {a : s0, b : t0}


def gcd(a,b):
    if a == b:
        return abs(a)
    coefs: dict[int: int] = bezout_coeffs(a, b)
    return abs((a * coefs[a]) + (b * coefs[b]))


""" ----------------- PROBLEM 1 ----------------- """



def mod_inv(a, m):
  """
  returns the smallest, positive inverse of a modulo m
  raises a ValueError if a and m are not relatively prime
  INPUT: a - integer
         m - positive integer
  OUTPUT: the inverse of a modulo m as an integer
  """
  if gcd(a, m) != 1:
    raise ValueError(f"The value {a} and {m} are not relatively prime.")
  inverse = bezout_coeffs(a, m).get(a)
  if inverse < 0:
    inverse += m
  return inverse


""" ----------------- PROBLEM 2 ----------------- """


def affine_encrypt(text, a, b):
  """
    encrypts the plaintext 'text', using an affine transformation key (a, b)
    INPUT:  text - plaintext as a string of letters
            a - integer satisfying gcd(a, 26) = 1.  
                Raises error if such is not the case
            b - integer 
            
    OUTPUT: The encrypted message as a string of characters
    """
  # FIXME: raise an error if the gcd(a, 26) is not 1
  if gcd(a, 26) != 1:
    raise ValueError("The given key is invalid.")

  cipher = ""
  for letter in text:
    if letter.isalpha():
      # FIXME: Use util.py to initialize 'num' to be
      # the integer corresponding to the current letter
      num = int(letters2digits(letter))

      # FIXME: Encrypt the current 'num' using the
      # affine transformation with key (a, b).
      # Store the result in cipher_digits.
      cipher_digits = str((num * a + b) % 26)

      if len(cipher_digits) == 1:
        # FIXME: If the cipherdigit is 0 - 9,
        # prepend the string with a 0
        # to make it a two-digit number
        cipher_digits = f"0{cipher_digits}"

      # FIXME: Use util.py to append to the cipher the ENCRYPTED letter
      # corresponding to the current cipher digits
      cipher += digits2letters(cipher_digits)

  return cipher


""" ----------------- PROBLEM 3 ----------------- """


def affine_decrypt(ciphertext, a, b):
  """
    decrypts the string 'ciphertext', which was encrypted using an affine 
    transformation key (a, b)
    INPUT:  ciphertext - a string of encrypted letters
            a - integer satisfying gcd(a, 26) = 1.  
            b - integer 
            
    OUTPUT: The decrypted message as a string of characters
    """
  a_inv = mod_inv(a, 26)

  text = ""
  for letter in ciphertext:
    if letter.isalpha():
      letter = letter.upper()

      # FIXME: Use util.py to find the integer `num` that corresponds
      # to the given letter
      num = int(letters2digits(letter))

      # FIXME: Decrypt the integer that corresponds to the current
      # encrypted letter using the decryption function for an affine
      # transformation with key (a, b) so that letter_digits holds
      # the decrypted number as a string of two digits
      letter_digits = str((a_inv * (num - b)) % 26)

      if len(letter_digits) == 1:
        # FIXME: If the letter number is between 0 - 9, inclusive,
        # prepend the string with a 0
        letter_digits = f"0{letter_digits}"

      # FIXME: Use util.py to append to the text the decrypted
      # letter corresponding to the current letter digits
      text += digits2letters(letter_digits)
  return text


""" ----------------- PROBLEM 4 ----------------- """


def encryptRSA(plaintext, n, e):
  """encrypts plaintext using RSA and the key (n, e)
    INPUT:  text - plaintext as a string of letters
            n - positive integer
            e - integer 
            
    OUTPUT: The encrypted message as a string of digits
    """
  text = plaintext.replace(' ', '')  # removing whitespace

  # FIXME: Use util.py to initialize 'digits' as a string of
  # the two-digit integers that correspond to the letters of 'text'
  digits = letters2digits(text)

  # FIXME: Use util.py to initialize 'l' with the length of each RSA block
  l = blocksize(n)

  # FIXME: Use a loop to pad 'digits' with enough 23's (i.e. X's)
  # so that it can be broken up into blocks of length l
  while len(digits) % l:
    digits += "23"

  # creating a list of RSA blocks
  blocks = [digits[i:i + l] for i in range(0, len(digits), l)]

  cipher = ""
  for b in blocks:
    # FIXME: Initialize 'encrypted_block' so that it contains
    # the encryption of block 'b' as a string
    encrypted_block = str((int(b) ** e) % n)

    if len(encrypted_block) < l:
      # FIXME: If the encrypted block contains less digits
      # than the block size l, prepend the block with enough
      # 0's so that the numeric value of the block
      # remains the same, but the new block size is l,
      # e.g. if l = 4 and encrypted block is '451' then prepend
      # one 0 to obtain '0451'
      encrypted_block = f"{'0'*(l-len(encrypted_block))}{encrypted_block}"

    # FIXME: Append the encrypted block to the cipher
    cipher += encrypted_block
  return cipher


""" ----------------- PROBLEM 5 ----------------- """


def decryptRSA(cipher, p, q, e):
  """decrypts the cipher, which was encrypted using RSA and the key (p * q, e)
    INPUT:  cipher - ciphertext as a string of digits
            p, q - prime numbers used as part of the key n = p * q to encrypt 
                   the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The decrypted message as a string of letters
    """
  n = p * q
  ciphertext = cipher.replace(' ', '')

  # FIXME: Use util.py to initialize `l` with the size of
  # each RSA block
  l = blocksize(n)

  # FIXME: Use a Python list comprehension to break the ciphertext
  # into blocks of equal length 'l'. Initialize 'blocks' so that it
  # contains these blocks as elements
  blocks = [cipher[i:i + l] for i in range(0, len(cipher), l)]

  text = ""  # initializing the variable that will hold the decrypted text

  # FIXME: Compute the inverse of e
  e_inv = mod_inv(e, (p-1) * (q-1))

  for b in blocks:
    # FIXME: Use the RSA decryption function to decrypt
    # the current block
    decrypted_block = str((int(b) ** e_inv) % n)

    if len(decrypted_block) < l:
      # FIXME: If the decrypted block contains less digits
      # than the block size l, prepend the block with
      # enough 0's so that the numeric value of the block
      # remains the same, but the new block size is l,
      # e.g. if l = 4 and decrypted block is '19' then prepend
      # two 0's to obtain '0019'
      decrypted_block = f"{'0'*(l-len(decrypted_block))}{decrypted_block}"

    # FIXME: Use util.py to append to text the decrypted block
    # transformed into letters
    text += digits2letters(decrypted_block)

  return text