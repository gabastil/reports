# usr/bin/python
# test.py
# Glenn Abastillas
# January 17, 2017
#
# The test.py class will be used to practice plotly implementations.
# The tutorial used for this script can be found at this URL:
# 	
#	> https://plot.ly/python/continuous-error-bars/
#

import plotly.plotly as plt
from plotly.graph_objs import *

# Set up the variables used in this script
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_rev = x[::-1]

# Line 1
y1 = [1,2,3,4,5,6,7,8,9,10]
y1_upper = [2,3,4,5,6,7,8,9,10,11]
y1_lower = [0,1,2,3,4,5,6,7,8,9]
y1_lower = y1_lower[::-1]

# Line 2
y2 = [5,2.5,5,7.5,10,12.5,15,17.5,20,22.5,]


