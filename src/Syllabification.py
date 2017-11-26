from Tkinter import *
from itertools import groupby
import tkFileDialog
import codecs
import sys
import re
import os
from IPAEquv import IPAEquivalent
from Labelchang1 import Labelchanger1
from Labelchang2 import Labelchanger2
from countvc import countvowel
reload(sys)
sys.setdefaultencoding('utf-8')
uvwl = {u'\u0259': 0, u'u': 0, u'E': 0, u'M': 0, u'A': 0, u'O': 0, u'\u0254': 0, "J": 0, "N": 0, u'i': 0, u'a': 0,
        u'U': 0, u'I': 0, u'!': 0, u'#': 0, u'%': 0, u'(': 0, u')': 0, u'_': 0, u'+': 0, u'=': 0, u'1': 0, u'`': 0}
uvwl1 = [u'\u0259', "u", "E", "A", "O", "M", "J", "N", u'i', u'a', "U", u'\u0254', "I", u'!', u'#', u'%', u'(', u')',
         u'_', u'+', u'=', u'1', u'`']
long_vowel = ["E", "A", "O", "M", "J", "N", "U", "I"]
short_vowel = ["i", "o", "u", u'\u0259']
uc = [u'p', u'b', u't', u'd', u'\u0288', u'\u0256', u't\u0283', u'd\u0292', u'k', u'g', u'q', u'm', u'n', u'\u0273',
      u'f', u's', u'z', u'\u0283', u'x', u'\u0263', u'h', u'\u028b', u'j', u'r', u'l', u'\u023f', u'\u027d', u'\u0272',
      u'\u014b']

ustop = [u'p', u'b', u't', u'k', u'd', u'g', u'P', u'K', u'G', u'D']
ucp = ["P", "B", "T", "D", "Q", "C", "c", "Z", "5", "K", "R", "G"]

def Syllabify(entries):
 IPAEquivalent(entries)
 hindi_output = (entries['Underlying Phonemic Form'].get()) 
 hindi_input_array1=hindi_output.split()
 flag=0
 flag_new=0
 temp=""
 temp1=[]
 temp2=[]
 temp3=""
 temp2.append(" ")
 temp6=[]
 for word in hindi_input_array1: 
  hindi_output=word
  hindi_output=Labelchanger1(hindi_output)
  countv,countc=countvowel(hindi_output)
  global consonantindexes
  consonantindexes=[]
  global vowelindexes
  vowelindexes=[]
  global indexvowels
  indexvowels=[]
  global indexvowelsnew
  indexvowelsnew=[]
  global indexconsonants
  indexconsonants=[]
  vowelindexes=list(set(hindi_output) & set(uvwl1))
  consonantindexes=list(set(hindi_output).difference(set(uvwl1)))
  for k in range(len(vowelindexes)):
	  for j in range(len(hindi_output)):
	      if (vowelindexes[k]==hindi_output[j]):
		  indexvowels.append(j)
		  indexvowels.sort()
  for k in range(len(consonantindexes)):
	  for j in range(len(hindi_output)):
	      if (consonantindexes[k]==hindi_output[j]):
		  indexconsonants.append(j)
		  indexconsonants.sort()
  global pos
  pos=[]	
   
  hindi_output=Labelchanger2(hindi_output)
  if (countv==1):
        entries['I-Level Syllabification'].delete(0,END)
	entries['I-Level Syllabification'].insert(0,hindi_output)
	
  else:
         
	hindi_output=Labelchanger1(hindi_output)
        for k in range(1,len(indexvowels)):
	      
	      if((indexvowels[k]-indexvowels[k-1])==2 or (indexvowels[k]-indexvowels[k-1])==1):
		    
		      pos += [indexvowels[k-1]]
		    
	      if(((indexvowels[k]-indexvowels[k-1])==3 or (indexvowels[k]-indexvowels[k-1]) == 4)):
		   	
		    
                        pos += [(indexvowels[k-1]) +1]
		      
	      if((indexvowels[k]-indexvowels[k-1]) == 5 or (indexvowels[k]-indexvowels[k-1]) == 6):
		      pos += [(indexvowels[k-1]) +2]
  
  length_pos=len(pos)
  for i in range(length_pos):
    pos[i]+=i+1
  global hindi_output1
  hindi_output1=[]
  hindi_output1=list(hindi_output)
  
  for i in range(0,length_pos):
    hindi_output1.insert(pos[i],'.')
  print "hindi_output after first syll", hindi_output1
  for i in range(1,len(hindi_output1)-1):
     for j in range(0, len(ustop)):
        if (hindi_output1[i]==ustop[j] and hindi_output1[i+1]=="." and (hindi_output1[i+2]=="r" or hindi_output1[i+2]=="l" or hindi_output1[i+2]==u'\u028b' or hindi_output1[i+2]=="j")):
              temp=hindi_output1[i+1]
              hindi_output1[i+1]=hindi_output1[i]
              hindi_output1[i]=temp
                        
  del pos[:]
  for i in range(0,len(hindi_output1)):
    if hindi_output1[i]==".":
       pos.append(i)
        
  hindi_output_syll=''.join(hindi_output1)
  hindi_output_syll=Labelchanger2(hindi_output_syll)
  if(flag>=1):
    hindi_output_syll=temp+hindi_output_syll
  flag+=1
  entries['I-Level Syllabification'].delete(0,END)
  entries['I-Level Syllabification'].insert(0,hindi_output_syll)
  temp=hindi_output_syll+" "
  for i in range(len(indexconsonants)):
    indexconsonants[i]+=i
  
 ########################################  End of Syllabification ########################################################################

