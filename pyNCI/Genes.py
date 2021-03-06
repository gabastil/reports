#!usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Name: 	Genes.py
# Version: 	1.0.0
# Author: 	Glenn Abastillas
# Date:		July 15, 2016

""" The Genes class reads in a file containing gene information required
for a search for specified genes in a document set. The class reads in a file,
which contains specifications for genes of interest. These include the gene's 
name, known variants, related drugs, and regular expressions associated with it.

This class can be used in conjunction with other NLP classes to find genetic
terms of interest in a document set.

This class utilizes the Spreadsheet class to open and retrieve data from tab
delimited spreadsheets. This class does not inherit any methods or data members
from the Spreadsheet class.
"""

import os, sys, re
sys.path.append("..")
from pyDocs.Spreadsheet import Spreadsheet
#print os.getcwd()

class Genes(object):

	"""
		To use the Genes Class, specify a tab-delimited text file upon object
		construction. The tab-delimited text file could be suffixed by the gene
		extension (*.gene) to distinguish it from other text files.

		The default initialization extracts regular expressions from the .gene
		file but this can be changed by changing the 'regex' parameter to False
		upon instantiation. 

		Retrieve the appropriate regular expressions by using the get-methods
		associated with the type of regular expression desired. 

		getGene() retrieves all regular expressions (variants, amino acid name(s), and
		related drugs).

		getDrugs() retrieves regular expressions from the 'related drugs' column
		in the *.gene document.

		getAmino() retrieves regular expressions from the 'amino acid' column in
		the *.gene document.
	"""

	def __init__(self, filePath="../../resources/biomarkers.gene", regex=True):
		""" initalize class 
			@param	filePath: path to .gene file containing gene specs
			@param	regex: if True, use 'regex' column in the .gene file
		"""
		genes_spreadsheet = Spreadsheet(filePath)

		gene_biomarker= genes_spreadsheet.getColumn("biomarker")
		gene_names	  = genes_spreadsheet.getColumn("gene")
		gene_variants = genes_spreadsheet.getColumn("variants")
		gene_drugs	  = genes_spreadsheet.getColumn("drugs")
		gene_aminos	  = genes_spreadsheet.getColumn("amino")

		self.genes = dict()
		self.drugs = dict()
		self.amino = dict()

		# If regex parameter is True, store the regex column
		if regex:
			gene_regexes = genes_spreadsheet.getColumn("regex")

			re_compile = re.compile

			# Loop through the gene names and add an entry for each name (variant names are assigned regexes as well)
			for i in xrange(len(gene_names)):
				gene_drug  = re_compile(gene_drugs[i].replace("; ", "|"))
				gene_amino = re_compile(gene_aminos[i].replace("; ", "|"))
				gene_regex = re_compile(gene_regexes[i])

				self.drugs[gene_names[i]] = gene_drug
				self.amino[gene_names[i]] = gene_amino
				self.genes[gene_names[i]] = gene_regex
				
				variants = gene_variants[i].replace("; ", "|")

				# Assign gene_regex for each variant of the original gene name as well.
				for variant in variants.split("|"):
					self.genes[variant] = gene_regex
					self.drugs[variant] = gene_drug
					self.amino[variant] = gene_amino

		# If regex parameter is False, store the variants column
		else:

			# Loop through the gene names and add an entry for each name (variant names are assigned literals as well)
			for i in xrange(len(gene_names)):
				variants = gene_variants[i].replace("; ", "|")
				drugs 	 = gene_drugs[i].replace("; ", "|")
				amino 	 = ["{}-amino acid".format(amino_acid) for amino_acid in gene_aminos[i].split("; ") if len(amino_acid) > 0]

				literal = r"({})|({})|({})".format(variants, drugs, "|".join(amino))
				literal = re.compile(literal)

				gene_drug  = re_compile(drugs)
				gene_amino = re_compile("|".join(amino))


				self.genes[gene_names[i]] = literal
				self.drugs[gene_names[i]] = gene_drug
				self.amino[gene_names[i]] = gene_amino

				# Assign literal for each variant of the original gene name as well.
				for variant in variants.split("|"):
					self.genes[variant] = literal
					self.drugs[variant] = gene_drug
					self.amino[variant] = gene_amino

	def getGene(self, gene):
		""" return regular expression for specified gene
			@param	gene: gene or variant name
		"""
		return self.genes[gene]

	def getDrugs(self, gene):
		""" return regular expression for drugs associated with specified gene
			@param	gene: gene or variant name
		"""
		return self.drugs[gene]

	def getAmino(self, gene):
		""" return regular expression for amino acids associated with specified gene
			@param	gene: gene or variant name
		"""
		return self.amino[gene]

if __name__=="__main__":
	print os.getcwd()

	g = Genes(filePath=u"../../resources/biomarkers.gene", regex=1)
	print g.getGene("HER-2")
	print g.getDrugs("HER-2").pattern
	print g.getAmino("HER-2").pattern