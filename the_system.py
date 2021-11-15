
import re
import csv
import pandas as pd

## Loading Of Stop Words in a List
stwrdl = open("StopWords_GenericLong.txt")
stlist = stwrdl.read().rstrip()
## Loading MasterDictionary
MDd = pd.read_csv("MasterDictionary.csv")

def cleanfood(food):
	food = food.replace(",",' ')
	food = food.replace(".",' ')
	food = food.replace("?",' ')
	food = food.replace("!",' ')
	tmp = food.split()
	for a in tmp:
		try:
			if stlist.index((a)) > -1:
				food = food.replace((" "+a+" ")," ")
		except ValueError:
			pass
	return food

#this function returns +ve, -ve, polarity and subjectivity scores
def PNPoS(food):
	nve, pve, po, sby = 0,0,0,0
	food = food.split()
	for a in food:
		try:
			tp = (MDd['Negative'][((list(MDd['Word'])).index(a.upper()))])
			if tp > 0:
				nve=nve+1
		except ValueError:
			pass
	for a in food:
		try:
			tp = (MDd['Positive'][((list(MDd['Word'])).index(a.upper()))])
			if tp > 0:
				pve=pve+1
		except ValueError:
			pass
	po = (pve - nve)/ ((pve + nve) + 0.000001)
	sby = (pve + nve)/((len(food)) + 0.000001)

	return [pve, nve, po, sby]

def syllables(food):
	scnt = 0
	vows = ['a','e','i','o','u']
	food = food.replace("es "," ")
	food = food.replace("ed "," ")
	for a in food:
		try:
			vows.index(a)
			scnt = scnt + 1
		except ValueError:
			pass
	return scnt

def SlCwF(food):
	nwd = (len(food.split()))		#number of words
	nse = (len(food.split('.')))	#number of sentences
	cmw = 0 						#number of complex words	
	for a in food.split():
		if syllables(a) > 2:
			cmw = cmw + 1

	avgse = nwd/nse								#average sentence length^2
	peccw = cmw/(len(food.split())+1)				#% of complex words
	fog = 0.4*(avgse/peccw)						#fog index
	sypw = syllables(food)/(len(food.split()))	#syllable per word
	food = food.replace(" ","")

	return [avgse, peccw, fog, cmw, sypw, len(food)/nwd]

def perspros(food):
	tmp = len(food)
	food = food.replace(" I "," ")
	food = food.replace(" I, "," ")
	food = food.replace(" we "," ")
	food = food.replace(" we, "," ")
	food = food.replace(" my "," ")
	food = food.replace(" ours "," ")
	food = food.replace(" us "," ")
	return [tmp - len(food)]