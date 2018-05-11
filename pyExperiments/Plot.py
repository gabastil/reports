import matplotlib.pyplot as plt
import random as r
import math

x = range(10)
y = [math.exp(n) for n in range(10)]
z = [r.random()*n**2 for n in range(10)]

plt.plot(x,y, "g--")
plt.axis([0,5,0,15])
plt.show()