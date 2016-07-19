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
print os.getcwd(), "TEST'"

class Report(object):

	def __init__(self, report=None, section=None, stopwords="resources\stopwords.txt"):
		#print "test"

		#self.__private = "test"

		# Report data: __report is a list of lines, which are lists of tokens. <SET,GET>
		# Report data: __report_xml_root ElemenTree object containing XML data. <SET,GET>
		self.__report 	   		= list()
		self.__report_xml_root  = None

		# Number of tokens and number of lines. <SET,GET>
		self.__report_tokens 	= 0
		self.__report_lines  	= 0

		# If the report is in XML, then 1. Otherwise, 0. <SET,GET>
		self.__report_type		= None
		self.__report_cleaned	= False

		# If the report is in XML, section to load as text <SET,GET>
		self.__report_section_of_interest = section

		# Paths to ancillary files <SET,GET>
		self.__stopwords		= stopwords

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
			print "It's an XML {}\\{}".format(os.getcwd(), report)
			#report = "{}\\{}".format(os.getcwd(), report)
			tree = XML.parse(report)
			self.__report_xml_root = tree.getroot()
			#self.__report = tree.getroot()

			#print "TEST", self.__report_xml_root

			#TEST
			for child in self.__report_xml_root:
				print child.tag, child.attrib

			self.focus(self.__report_section_of_interest)
			self.__report_type = 1


		else:
			split = str.split
			with open(report, 'r') as r:
				opened_report = r.read()
				self.__report = [line.split() for line in opened_report.split('\n') if len(line) > 0]
				self.__report_type = 0

		#print self.__report
		self.__refresh()

	def __refresh(self):
		""" update report_tokens and report_lines variables """
		self.__report_tokens= sum((len(line) for line in self.__report))
		self.__report_lines	= len(self.__report)

	def focus(self, section):
		""" change the report section of interest for xml reports 
			@param	section: name of section name
			@return	None if section is found
			@raise	IndexError if section is not found
		"""

		# Loop through the different children of XML Root.
		for report_section in self.__report_xml_root:

			# If the XML Child node's name matches the section specified, set self.__report to that section's text.
			if report_section.get('name').lower()==section.lower() or report_section.get('full').lower()==section.lower():
				self.__report = [line.split() for line in report_section.get('text').split('\\n') if len(line) > 0]
				#print "focus()", self.__report, report_section.getchildren()
				#print "Text switched to {}".format(report_section.get('name').upper())
				self.__refresh()
				return None

		raise IndexError("Specified section does not exist or section is not specified (e.g., section=None).")

	def count(self, term=None, case_sensitive=True):
		""" get a count of the specified term in the report
			@param	term: term to count in the report
			@param	case_sensitive: make search case sensitive
			@report integer count
		"""
		# If no term is specified, return the total number of tokens in self.__report.
		if term is None:
			return self.__report_tokens

		# If case_sensitive is true, term must match token case.
		if case_sensitive:
			return sum((line.count(term) for line in self.__report))
		else:
			reports_lower_case = [[token.lower() for token in line] for line in self.__report]
			return sum((line.count(term) for line in reports_lower_case))

	def getReport(self, xml=False):
		""" return object data 
			@param	xml: return  self.__report_xml_root if true
			@return self.__report
		"""
		# If xml not specified, return just the text.
		if not xml:
			return self.__report

		# If xml specified, return the ElementTree object
		else:
			return self.__report_xml_root

	#def getPrivate(self):
	#	return self.__private

	def getType(self):
		""" get report type, xml or txt (includes non-xml) 
			@return	'xml' or 'txt' to indicate report type
		"""
		if self.__report_type:
			return "xml"
		
		return "txt"
		
	def setSection(self, section):
		""" set the report section of interest for xml reports """
		self.__report_section_of_interest = section
		self.focus(self.__report_section_of_interest)

	def setStopwords(self, stopwords):
		""" set the path to the stopwords """


if __name__=="__main__":
	#t = Report("resources\\test.txt")
	#print t.__report_tokens
	#print t.__report_lines
	#print t.__report_counts
	#t.__report = [[1,2,3,4],[1,2,3]]
	#t._Report__refresh()
	#print t.__report_tokens
	#print t.__report_lines
	#print t.__report_counts
	#print "len()", len(t)
	#print t.getReport()
	#print len(t)

	#k = Report("resources/health.xml", "HPI")
	#os.chdir("H:/PROJECTS/Python/pyNCI/resources")
	print os.getcwd()
	k = Report("resources\\test2.xml")
	#print dir(k.getReport().getchildren()[0].getchildren()[0])
	#print k.report.getchildren()[0].get(1)
	#print "k.private", k.getPrivate()
	#print len(k)
	#print "count()", k.count('the',0)
	#k.focus("PMH")
	#print k.getReport()
	#print len(k)
	#print ["the", "patient"].count("patient")

	#k.setSection("HPI")
	#print k.getReport(); print len(k); print "TYPE:", k.getType()