#!usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Name: 	Document.py
# Version: 	1.0.0
# Author: 	Glenn Abastillas
# Date:		June 29, 2016

""" The Report class is intended to be a base class that holds clinical 
documentation read in as an XML or TXT file.
"""

import os, re
import xml.etree.ElementTree as XML
print os.getcwd(), "TEST'"

class Document(object):

	def __init__(self, report=None, section=None, stopwords="resources\stopwords.txt"):

		# Paths to ancillary files <SET,GET>
		self.__stopwords = stopwords

		self.document = None

		# Regular expressions
		self.open_tag  = re.compile(r"<(?!/)\w+>")
		self.close_tag = re.compile(r"</\w+>")

		if report is not None:
			self.document = self.__initialize(*self.__open(report))

	def __len__(self):
		""" return number of tokens in document """
		return self.document_tokens

	def __open(self, report=None):
		""" return opened report and tags with pairs
			@param	report: path to report (XML)
		"""
		# Compile regular expressions for opening and closing tags
		open_tag  = self.open_tag
		close_tag = self.close_tag

		# Open and read report and get a set of open_tag and close_tag strings
		with open(report, "rb") as opened_report:

			opened_report = opened_report.read()

			open_tags  = list(set(open_tag.findall(opened_report)))
			close_tags = list(set(close_tag.findall(opened_report)))

		# Get _tags set that contains the most tags
		if len(open_tags) > len(close_tags):
			tags = open_tags
			other_tags = [tag.replace("/", "") for tag in close_tags]
		else:
			tags = [tag.replace("/", "") for tag in close_tags]
			other_tags = open_tags

		# Replace characters with new line
		opened_report = opened_report.replace("\X0D\\", "\n")
		opened_report = opened_report.replace("\X0A\\", "\n")
		opened_report = opened_report.replace("\n\n", "\n")

		all_tag_pairs = [(tag, close_tags[other_tags.index(tag)]) for tag in tags if tag in other_tags]

		return opened_report, all_tag_pairs

	def __initialize(self, opened_report, complete_tags=None):
		""" open and process file indicated in report variable 
			@param	complete_tags: path to report file.
		"""

		indices_unsorted = list()
		indices_unsorted_extend = indices_unsorted.extend

		# Loop through the tag pairs
		for open_tag, close_tag in complete_tags:

			index_start = [index.start() for index in re.finditer(open_tag,  opened_report)]
			index_end 	= [index.end() 	 for index in re.finditer(close_tag, opened_report)]

			# If there are more index_starts than index_ends, get indices for start and ends (may change this in the future)
			if len(index_start) > len(index_end):
				span_information = [(index_start[x], index_end[x], open_tag) for x in xrange(len(index_end))]
			else:
				span_information = [(index_start[x], index_end[x], open_tag) for x in xrange(len(index_start))]
			
			indices_unsorted_extend(span_information)

		#indices_sorted = list()
		#indices_sorted_extend = indices_sorted.extend

		#for index_list in indices_unsorted:
		#	indices_sorted_extend(sorted(index_list, key=lambda x:x[0]))

		indices_sorted = sorted(indices_unsorted, key=lambda x:x[0])

		sections = list()
		sections_append = sections.append

		for span in indices_sorted:
			new_section = Section(span[-1], opened_report[span[0]:span[1]])
			sections_append(new_section)

		#print len(sections)
		#print sections[:10]
		#print sections[6587].getTag()
		print sections[6587].getContent()
		return sections


	def __hasTags(self, span):
		""" return True if span has XML tags """
		#print "__hasTags?", span, type(span)
		#span = str(span)
		if span is None or len(span)==0 or type(span)!=type(str):
			return False


		if len(self.open_tag.search(span)) > 0 or len(self.close_tag.search(span)) > 0:
			return True
		return False

	def __refresh(self):
		""" update report_tokens and report_lines variables """
		self.document_tokens= sum((len(line) for line in self.document))
		self.document_lines	= len(self.document)

	def focus(self, section):
		""" change the report section of interest for xml reports 
			@param	section: name of section name
			@return	None if section is found
			@raise	IndexError if section is not found
		"""

		# Loop through the different children of XML Root.
		for report_section in self.document_xml_root:

			# If the XML Child node's name matches the section specified, set self.document to that section's text.
			if report_section.get('name').lower()==section.lower() or report_section.get('full').lower()==section.lower():
				self.document = [line.split() for line in report_section.get('text').split('\\n') if len(line) > 0]
				#print "focus()", self.document, report_section.getchildren()
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
		# If no term is specified, return the total number of tokens in self.document.
		if term is None:
			return self.document_tokens

		# If case_sensitive is true, term must match token case.
		if case_sensitive:
			return sum((line.count(term) for line in self.document))
		else:
			reports_lower_case = [[token.lower() for token in line] for line in self.document]
			return sum((line.count(term) for line in reports_lower_case))

	def getDocument(self, xml=False):
		""" return object data 
			@param	xml: return  self.document_xml_root if true
			@return self.document
		"""
		# If xml not specified, return just the text.
		if not xml:
			return self.document

		# If xml specified, return the ElementTree object
		else:
			return self.document_xml_root

	#def getPrivate(self):
	#	return self.__private

	def getType(self):
		""" get report type, xml or txt (includes non-xml) 
			@return	'xml' or 'txt' to indicate report type
		"""
		if self.document_type:
			return "xml"
		
		return "txt"
		
	def setSection(self, section):
		""" set the report section of interest for xml reports """
		self.document_section_of_interest = section
		self.focus(self.document_section_of_interest)

	def setStopwords(self, stopwords):
		""" set the path to the stopwords """



class Section(object):

	def __init__(self, tag, content, rank=0, span=0):
		""" initialize Section object 
			@param	tag: String name of XML tag
			@param	content: String content of XML tag section
			@param	rank: order of instantiation
			@param	span: beginning and ending indices of text span
		"""
		self.tag = tag
		self.rank = rank
		self.span = span

		content = re.sub(r"</\w+>", "", content).strip().replace("  ", " ")
		self.content = re.sub(r"<(?!/)\w+>","", content).strip()

		#self.content = [token for token in content.split() if len(token) > 0]

	def getContent(self):
		""" return object's self.content variable """
		return self.content

	def getRank(self):
		""" return object's self.rank variable """
		return self.rank

	def getSpan(self):
		""" return object's self.span variable """
		return self.span

	def getTag(self):
		""" return object's self.tag variable """
		return self.tag

if __name__=="__main__":
	#t = Document("resources\\test.txt")
	#print t.document_tokens
	#print t.document_lines
	#print t.document_counts
	#t.document = [[1,2,3,4],[1,2,3]]
	#t._Report__refresh()
	#print t.document_tokens
	#print t.document_lines
	#print t.document_counts
	#print "len()", len(t)
	#print t.getReport()
	#print len(t)

	#k = Document("resources/health.xml", "HPI")
	#os.chdir("H:/PROJECTS/Python/pyNCI/resources")
	print os.getcwd()
	k = Document("resources\\test.xml")
	#print dir(k.Document().getchildren()[0].getchildren()[0])
	#print k.report.getchildren()[0].get(1)
	#print "k.private", k.getPrivate()
	#print len(k)
	#print "count()", k.count('the',0)
	#k.focus("PMH")
	#print k.Document()
	#print len(k)
	#print ["the", "patient"].count("patient")

	#k.setSection("HPI")
	#print k.Document(); print len(k); print "TYPE:", k.getType()