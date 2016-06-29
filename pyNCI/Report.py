#!usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Name: 	Report.py
# Version: 	1.0.0
# Author: 	Glenn Abastillas
# Date:		June 29, 2016

""" The Report class is intended to be a base class that holds clinical 
documentation read in as an XML or TXT file.
"""

import os
import xml.etree.ElementTree as XML

class Report(object):

	def __init__(self, report=None, section=None):
		print "test"

		self.__private = "test"

		self.__report 	   		= list()
		self.__report_xml_root  = None

		self.__report_tokens 	= 0
		self.__report_lines  	= 0

		# If the report is in XML, then 1. Otherwise, 0.
		self.__report_type		= None
		self.__report_cleaned	= False

		self.__report_section_of_interest = section

		self.__initialize(report)

	def __len__(self):
		""" return number of tokens in document """
		return self.__report_tokens

	def __initialize(self, report=None):
		""" open and process file indicated in report variable 
			@param	report: path to report file.
		"""

		extension = report.split('.')[-1].lower()

		# If the extension is xml, open with xml.xtree.ElementTree parser.
		# Otherwise, open as a text file.
		if extension=="xml":
			print "It's an XML"
			tree = XML.parse(report)
			self.__report_xml_root = tree.getroot()
			self.__report = tree.getroot()
			self.focus(self.__report_section_of_interest)
			self.__report_type = 1
		else:
			split = str.split
			with open(report, 'r') as r:
				opened_report = r.read()
				self.__report = [line.split() for line in opened_report.split('\n') if len(line) > 0]
				self.__report_type = 0

		self.__refresh()

	def __refresh(self):
		""" update report_tokens and report_lines variables """

		if self.__report_type=="xml":
			self.__report_tokens= ""
		else:
			self.__report_tokens= sum((len(line) for line in self.__report))
			self.__report_lines	= len(self.__report)

	def focus(self, section):
		""" change the report section of interest for xml reports 
			@param	section: name of section name
		"""

		# Loop through the different children of XML Root.
		for report_section in self.__report_xml_root:

			# If the XML Child node's name matches the section specified, set self.__report to that section's text.
			if report_section.get('name').lower()==section.lower() or report_section.get('full').lower()==section.lower():
				self.__report = report_section.get(section)


	def getCount(self, term=None):
		""" get a count of the specified term in the report
			@param	term: term to count in the report
			@report integer count
		"""

		if term is None:
			return self.__report_tokens

		return sum((line.count(term) for line in self.__report))

	def getReport(self):
		""" return object data 
			@return self.__report
		"""
		return self.__report

	def getPrivate(self):
		return self.__private

	def setFocus(self, section):
		""" set the report section of interest for xml reports """
		self.__report_section_of_interest = section


if __name__=="__main__":
	t = Report("resources/test.txt")
	#print t.__report_tokens
	#print t.__report_lines
	#print t.__report_counts
	#t.__report = [[1,2,3,4],[1,2,3]]
	#t._Report__refresh()
	#print t.__report_tokens
	#print t.__report_lines
	#print t.__report_counts
	#print "len()", len(t)
	print t.getReport()
	print len(t)

	k = Report("resources/health.xml", "phi")
	print dir(k.getReport().getchildren()[0].getchildren()[0])
	#print k.report.getchildren()[0].get(1)
	print "k.private", k.getPrivate()
	k.getCount()

	for s in k.getReport():
		if s.get('name').lower()=='hpi':
			print s, "YES"

		print s.get('name')