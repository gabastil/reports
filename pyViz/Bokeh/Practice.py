#!/usr/bin/python
#-*- encoding: utf-8 -*-
#	
#	Practice.py
#	Glenn Abastillas
#	September 3, 2016
#	Version 1.0
#	
#	This class contains methods related to Bokeh data visualization tools for practice.
#	

from bokeh.plotting import figure, output_file, show
import random
import numpy as np

class Practice(object):

	def __init__(self):
		pass

	def method(self):
		pass

if __name__=="__main__":

	""" 
	The Practice() class is not functioning for now. All Bokeh practice is scripted below.
	"""

	print np.random.random_integers(80,100,10)

	x = range(11)
	y = random.sample(range(80,100), 10)
	z = np.random.random_integers(80,100,10).tolist()

	output_file(".\\output\\bokeh_text.html")

	p = figure(title="line example", x_axis_label="Number of students", y_axis_label="Test Scores", x_range=[0,10], y_range=[min(z),100])
	p.line(x,z,legend="Scores and Students", line_width=5)
	p.line(x,[sum(y)/(len(y)*1.) for number in x],legend="Mean Score", line_width=2, line_color="red", line_dash="2 2")
	show(p)