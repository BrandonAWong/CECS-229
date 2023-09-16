""" ----------------- PROBLEM 1 ----------------- """
def primes(a, b):
    """
    prints all primes in the range [a, b]
    """
    if a < 1 or b < a: # handling invalid range
        raise ValueError("Invalid range given")
        
    if a == 1: # handling starting point a = 1
        a = 2  # this ensures 1 is not listed as a prime
    
    # FIXME: initialize `stop` which is the stopping criteria for 
    #        the loop in the Sieve of Eratosthenes
    stop = int(b ** (0.5))+1
    
    # FIXME: initialize a Python set called `primes` that contains 
    #        all integers in the range [a, b]
    P = set(range(a, b+1))
    
    for x in range(2, stop):
        
        # FIXME: use Python list comprehension to create a set 
        #        of multiples of x in the range [2, b];
        # HINT: the set of multiples of x can be expressed as 
        #       k * x, where k is an integer; hence the comprehension 
        #       should loop over values that satisfy k * x <= b
        multiples_x = set([k for k in range(b, a-1, -1) if k%x == 0 and k != x])
        P -= multiples_x  # removing the multiples of x from the set P

    return P


""" ----------------- PROBLEM 2 ----------------- """
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
        s1 = "FIXME: Replace this string"
        
        # FIXME: Update t1 according to the formula for tk
        t1 = "FIXME: Replace this string"
        
        s0 = temp_s
        t0 = temp_t
        temp = bk
        
        # FIXME: Update bk and ak
        bk = "FIXME: Replace this string"
        ak = "FIXME: Replace this string"
    
    # FIXME: Replace each string with the correct coefficients of a and b
    return {a : "FIXME: replace this string", b : "FIXME: replace this string"}


""" ----------------- PROBLEM 3 ----------------- """
def gcd(a,b):
    a, b = max(a,b), min(a,b)
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b