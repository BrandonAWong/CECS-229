import math

""" ----------------- PROBLEM 1 ----------------- """
def translate(S, z0):
	"""
	translates the complex numbers of set S by z0
	INPUT: 
		* S - set of complex numbers
		* z0 - complex number
	OUT:
		* a set consisting of points in S translated by z0
	"""
	return {p + z0 for p in S}


""" ----------------- PROBLEM 2 ----------------- """
def scale(S, k):
	"""
	scales the complex numbers of set S by k.  
	INPUT: 
		* S - set of complex numbers
		* k - positive float, raises ValueError if k <= 0
	OUT:
		* T - set consisting of points in S scaled by k
		
	"""
	if k <= 0:
		raise ValueError
	return {p * k for p in S}



""" ----------------- PROBLEM 3 ----------------- """
def rotate(S, tau):
	"""
	rotates the complex numbers of set S by tau radians.  
	INPUT: 
		* S - set of complex numbers
		* tau - float. If negative, the rotation is clockwise. If positive the rotation is counterclockwise. 
				If zero, no rotation.
	OUT:
		* a set consisting of points in S rotated by tau radians
		
	"""
	return {(p * math.e**(tau * 1j)) for p in S}


""" ----------------- PROBLEM 4 ----------------- """
class Vec:

	def __init__(self, contents=[]):
		"""
		Constructor defaults to empty vector
		INPUT: list of elements to initialize a vector object, defaults to empty list
		"""
		self.elements = contents
		return

	def __abs__(self):
		"""
		Overloads the built-in function abs(v)
		returns the Euclidean norm of vector v
		"""
		return sum([e**2 for e in self.elements])**(1/2)

	def __add__(self, other):
		"""
        overloads the + operator to support Vec + Vec
        RAISES ValueError if vectors are not same length 
        RETURNS a Vec object that is the sum vector of this Vec and 'other' Vec
        """
		if len(self.elements) != len(other.elements):
			raise ValueError
		contents = [self.elements[i] + other.elements[i] for i in range(len(self.elements))]
		return Vec(contents)

	def __sub__(self, other):
		"""
        overloads the - operator to support Vec - Vec
        RAISES ValueError if vectors are not same length 
        RETURNS a Vec object that is the difference vector of this Vec and 'other' Vec
        """
		if len(self.elements) != len(other.elements):
			raise ValueError
		return Vec([self.elements[i] - other.elements[i] for i in range(len(self.elements))])

	def __mul__(self, other):
		"""
        Overloads the * operator to support 
            - Vec * Vec (dot product) raises ValueError if vectors are not 
              same length in the case of dot product; returns scalar
            - Vec * float (component-wise product); returns Vec object
            - Vec * int (component-wise product); returns Vec object
            
        """
		if type(other) == Vec:  #define dot product
			if len(self.elements) != len(other.elements):
				raise ValueError
			return sum([self.elements[i] * other.elements[i] for i in range(len(self.elements))])

		elif type(other) == float or type(other) == int:  #scalar-vector multiplication
			return Vec([e * other for e in self.elements])

	def __rmul__(self, other):
		"""Overloads the * operation to support 
            - float * Vec; returns Vec object
            - int * Vec; returns Vec object
        """
		return Vec([e * other for e in self.elements])

	def __str__(self):
		"""returns string representation of this Vec object"""
		return str(self.elements)  # does NOT need further implementation
