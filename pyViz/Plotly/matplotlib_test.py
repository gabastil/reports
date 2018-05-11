import matplotlib.pyplot as plt
import numpy as np
# import random

x = np.random.random_sample(50) * 50
y = np.random.random_sample(50) * 50

ticks_int = [i for i in xrange(50) if not (i % 5)]
ticks_str = ["{}B".format(i) for i in xrange(50) if not (i % 5)]

# HISTOGRAM EXAMPLE
plt.hist(x, bins=100)
plt.xlabel("Random numbers for X")
plt.ylabel("Random numbers for Y")
plt.title("Histogram Test")
plt.yticks(ticks_int, ticks_str)
plt.show()

# HISTOGRAM 2D EXAMPLE
plt.hist2d(x, x * 2, bins=20)
plt.show()

# SCATTERPLOT EXAMPLE
plt.scatter(x, y, )
plt.xscale('log')
plt.xlabel("Random numbers for X")
plt.ylabel("Random numbers for Y")
plt.title("Scatter Plot Test")
plt.yticks(ticks_int, ticks_str)
plt.show()

# BOXPLOT EXAMPLE
plt.boxplot([x, x * 2, x / 2.5], showmeans=True)
plt.show()
