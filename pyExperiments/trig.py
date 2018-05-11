import math
def fact(number):
	product = 1.
	#print range(number), number
	for n in xrange(number):
		product *= (n+1)

	return product

def isOdd(number):
	if number % 2 == 0:
		return False
	return True

def sin(x):

	total = 0
	lastTermNeg = True

	for i in xrange(250):
		n = i+1

		if isOdd(n):
			coeff = fact(n)
			if not lastTermNeg:
				coeff *= -1

			variable = (x**n)/coeff

			total += variable
			lastTermNeg = not lastTermNeg


	return round(total,10)

def cos(x):

	#print x%(2*math.pi)
	x %= (2*math.pi)

	total = 0.
	#lastTermNeg = True

	for i in xrange(250):
		coefficient = 1./fact((2*i))
		leading_one = (-1)**i
		variable_x	= x**(2*i)

		total += coefficient*leading_one*variable_x
		#n = i+1

		#if not isOdd(n):
		#	coeff = fact(n)
		#	if lastTermNeg:
		#		coeff *= -1

		#	variable = (x**n)/coeff

		#	total += variable
		#	lastTermNeg = not lastTermNeg


	return round(total,10)

def e(x):
	total = 1

	for i in xrange(250):
		n=i+1
		total += (x**n)/fact(n)

	#if type(total)==type(1j):
		#total.real = round(total.real, 15)
		#total.imag = round(total.imag, 15)
		#print type(total), total.real, total.imag

	return total


print isOdd(3)
print fact(3)
#print "sin",sin(math.pi/4)
print "cos",cos(math.pi*.33333333333)
#print e(1j*math.pi)*(1-1j)