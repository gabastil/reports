import math

class Distance(object):

	def chebyshev(self):
		pass

	def cosine(self, vector1, vector2):
		""" return the Cosine Similarity between two vectors """

		# If vectors are of difference sizes, raise error
		if len(vector1)!=len(vector2):
			raise ValueError("Vectors must be of equal length")

		numerator = self.dot(vector1, vector2)
		denominator = self.magnitude(vector1) * self.magnitude(vector2)

		#print numerator, denominator
		return numerator/denominator

	def magnitude(self, vector):
		return math.sqrt(sum(element**2 for element in vector))

	def dot(self, vector1, vector2):
		""" return dot product of two vectors """

		# If vectors are of difference sizes, raise error
		if len(vector1)!=len(vector2):
			raise ValueError("Vectors must be of equal length")

		# Return sum of products of each element
		return sum(element1*element2 for element1, element2 in zip(vector1, vector2))

	def euclidean(self, vector1, vector2):
		""" return the Euclidean distance between two equal length vectors """
		
		# If vectors are of difference sizes, raise error
		if len(vector1)!=len(vector2):
			raise ValueError("Vectors must be of equal length")

		return math.sqrt(sum(((element1-element2)**2 for element1, element2 in zip(vector1,vector2))))

	def hamming(self, vector1, vector2):
		""" return the Hamming distance between two equal length vectors """
		
		# If vectors are of difference sizes, raise error
		if len(vector1)!=len(vector2):
			raise ValueError("Vectors must be of equal length")

		# Return sum of comparison of each element
		return sum(element1 != element2 for element1, element2 in zip(vector1, vector2))

	def levenshtein(self, vector1, vector2):
		""" return the Levenshtein distance between two equal length vectors """

		# Return distance of 0 if vectors are exactly the same
		if vector1==vector2: return 0

		# If the vectors are of the same length, use hamming distance
		if len(vector1)==len(vector2): return self.hamming(vector1, vector2)

		# Sort vectors with smallest at index 0 and largest at index 1
		v = sorted((vector1, vector2), key=len)

		# If the shortest vector is of length 0, return length of larger vector
		if len(v[0])==0: return len(v[0])

		prior = range(len(v[1])+1)

		# Loop through the longer vector
		for i, character in enumerate(v[1]):

			current = [i+1]

			# Loop through the shorter vector
			for j, character_2 in enumerate(v[0]):
				#print i, j,j+1, prior, prior[4]
				insertions 	= prior[j+1] + 1
				deletions 	= current[j] + 1
				substitutes = prior[j] + (character!=character_2)

				current.append(min(insertions, deletions, substitutes))
				
				#print prior, current, i, j
				#print insertions, deletions, substitutes

			prior = current

		return prior[-1]

	def manhattan(self, vector1, vector2):
		""" return Manhattan distance between two vectors """

		# If the vectors are strings, convert strings to numbers
		if type(vector1)!=type(list()) or type(vector2)!=type(list()):
			vector1 = [ord(element) for element in vector1]
			vector2 = [ord(element) for element in vector2]

		# If vectors are of difference sizes, raise error
		if len(vector1)!=len(vector2):
			raise ValueError("Vectors must be of equal length")

		#vectors = sorted((vector1,vector2), key=len)

		# Return sum of comparison of each element
		return sum(abs(element1-element2) for element1, element2 in zip(vector1,vector2))

if __name__=="__main__":
	d = Distance()

	print d.hamming([1,2,3,4], [1,2,4,4])
	print d.levenshtein("hi", "h3i")
	print d.levenshtein("hi", "hi3")
	print d.manhattan([1,2,3],[2,4,6])
	print d.cosine([1,-5],[1,3])
	print d.magnitude([1,1,1])