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
from Syllabification import Syllabify
from Syll_label import Labeling
reload(sys)
sys.setdefaultencoding('utf-8')
global hindi_output
hindi_output = []
global hindi_output1
hindi_output1 = []
global count_strong_syllable
count_strong_syllable=0
global count_weak_syllable
count_weak_syllable=0
strong_syll_pos=[]
global count_superstrong_syllable
count_superstrong_syllable=0
superstrong_syll_pos=[]
hindi_output1=[]
countv=0
global count_weak_syllable3
count_weak_syllable3=0
weak_syll_pos3=[]
global count_strong_syllable3
count_strong_syllable3=0
strong_syll_pos3=[]
global count_superstrong_syllable3
count_superstrong_syllable3=0
superstrong_syll_pos3=[]
global hindi_output_list
hindi_output_list=[]
def Phoneme(entries):
  Labeling(entries)
  hindi_output=(entries['Prosodic Label(PLSB)'].get()).rstrip()
  #hindi_output2 = Labelchanger1(hindi_output)
  hindi_output1=list(hindi_output)
  print "phoneme", hindi_output1
  count_final_strong_syll=0
  final_strong_syll=[]
  for i in range(len(hindi_output1)):
      if(hindi_output1[i]==u'\u03c3' and hindi_output1[i+1]==u'\u02b7'):
	hindi_output1[i]="@"
        hindi_output1[i+1]=""
      elif((hindi_output1[i]==u'\u03c3' and hindi_output1[i+1]==u'\u02b0')):
        hindi_output1[i]="$"
        hindi_output1[i+1]=""
      elif(hindi_output1[i]==u'\u03c3' and hindi_output1[i+1]==u'\u02e2' and hindi_output1[i+2]==u'\u02b0'):
	hindi_output1[i]="&"
        hindi_output1[i+1]=""
        hindi_output1[i+2]=""

  hindi_output_syllab=''.join(hindi_output1)
  hindi_output_syllab=hindi_output_syllab.replace("(","oon")
  hindi_output_syllab=hindi_output_syllab.replace(")","oun")
  hindi_output_syllab=hindi_output_syllab.replace("*",u'<\u03c3\u02e2>')
  hindi_output_syllab=hindi_output_syllab.replace(u'x',"kx") #for kha nuktha wala
  hindi_output_syllab=hindi_output_syllab.replace("I","ii")
  hindi_output_syllab=hindi_output_syllab.replace("A","aa")
  hindi_output_syllab=hindi_output_syllab.replace("E","e")
  hindi_output_syllab=hindi_output_syllab.replace("O","o")
  hindi_output_syllab=hindi_output_syllab.replace("U","oo")
  hindi_output_syllab=hindi_output_syllab.replace("M","au")
  hindi_output_syllab=hindi_output_syllab.replace("J","ei")
  hindi_output_syllab=hindi_output_syllab.replace("N","ou")
  hindi_output_syllab=hindi_output_syllab.replace("P","ph")#for Pha
  hindi_output_syllab=hindi_output_syllab.replace("B","bh")#for bha
  hindi_output_syllab=hindi_output_syllab.replace("T","th")#For ta
  hindi_output_syllab=hindi_output_syllab.replace("D","dh")#for dha
  hindi_output_syllab=hindi_output_syllab.replace("Q","txh") #for retroflex txh
  #hindi_output_syllab=hindi_output_syllab.replace("c",u't\u0283') #for ch(affiricate)
  hindi_output_syllab=hindi_output_syllab.replace("C","ch")#for chha
  hindi_output_syllab=hindi_output_syllab.replace("Z","jh")#for jha
  hindi_output_syllab=hindi_output_syllab.replace("j","y")#for ja
  hindi_output_syllab=hindi_output_syllab.replace("5","j")#for ja
  hindi_output_syllab=hindi_output_syllab.replace("K","kh")#for Kha
  hindi_output_syllab=hindi_output_syllab.replace("R","dxh") #for Rha
  hindi_output_syllab=hindi_output_syllab.replace("G","gh")
  hindi_output_syllab=hindi_output_syllab.replace("!","in")
  hindi_output_syllab=hindi_output_syllab.replace("#","iin")
  hindi_output_syllab=hindi_output_syllab.replace("%","un")
  hindi_output_syllab=hindi_output_syllab.replace("_","en")
  hindi_output_syllab=hindi_output_syllab.replace("+","ein")
  hindi_output_syllab=hindi_output_syllab.replace("=","aan")
  hindi_output_syllab=hindi_output_syllab.replace("7","on")
  hindi_output_syllab=hindi_output_syllab.replace(u'`',"an")
  hindi_output_syllab=hindi_output_syllab.replace(u'X',"n")
  hindi_output_syllab=hindi_output_syllab.replace(u'q',"gx")
  hindi_output_syllab=hindi_output_syllab.replace(u'\u0273',"nx")
  hindi_output_syllab=hindi_output_syllab.replace(u'\u0259', "a")
  hindi_output_syllab=hindi_output_syllab.replace(u'\u0288', "tx")
  hindi_output_syllab=hindi_output_syllab.replace(u'\u0283',"sh")
  hindi_output_syllab=hindi_output_syllab.replace(u'\u023f', "sx")
  hindi_output_syllab=hindi_output_syllab.replace(u'\u027d',"rx")
  hindi_output_syllab=hindi_output_syllab.replace(u'\u028b',"v")
  hindi_output_syllab=hindi_output_syllab.replace(u'\u0256',"dx")
  countlabel=0
  
  for i in range(len(hindi_output1)):
    
    if(hindi_output1[i]=="@" or hindi_output1[i]=="$" or hindi_output1[i]=="&"):
       countlabel+=1
  hindi_output_syllab=list(hindi_output_syllab)
  for i in range (len(hindi_output_syllab)):
        #if((hindi_output_syllab[i]=="$" and i!=final_strong_syll[len(final_strong_syll)-1])  or hindi_output_syllab[i]=="&"):
	    # hindi_output_syllab[i]="'" 
        if(countlabel==2):
          if(hindi_output_syllab[i]=="@" and hindi_output_syllab[i+2]=="$"  ):
             print"aao1"
             hindi_output_syllab[i]="1"
	  elif(hindi_output_syllab[i]=="@"):
	     hindi_output_syllab[i]="0"
          if(hindi_output_syllab[i]=="$"): 
             hindi_output_syllab[i]="0"
        if(countlabel==2):
         if(i+3!=""):
          if(hindi_output_syllab[i]=="@" and hindi_output_syllab[i+3]=="$"  ):
             print"aao1"
             hindi_output_syllab[i]="1"
	  elif(hindi_output_syllab[i]=="@"):
	     hindi_output_syllab[i]="0"
          if(hindi_output_syllab[i]=="$"): 
             hindi_output_syllab[i]="0"
          
        if(countlabel>=3):
          if(hindi_output_syllab[i]=="$" and (hindi_output_syllab[i+2]=="$"  or hindi_output_syllab[i+2]=="@" or hindi_output_syllab[i+2]=="&" )):
             hindi_output_syllab[i]="1"
          elif(hindi_output_syllab[i]=="$"): 
             hindi_output_syllab[i]="0"
          if(hindi_output_syllab[i]=="@"): 
             hindi_output_syllab[i]="0"
          
        if(countlabel>=3):
         if(i+3!=""):
          if(hindi_output_syllab[i]=="$" and (hindi_output_syllab[i+3]=="$"  or hindi_output_syllab[i+3]=="@" or hindi_output_syllab[i+3]=="&" )):
             hindi_output_syllab[i]="1"
          elif(hindi_output_syllab[i]=="$"): 
             hindi_output_syllab[i]="0"
          if(hindi_output_syllab[i]=="@"): 
             hindi_output_syllab[i]="0"
          if(hindi_output_syllab[i]=="&"): 
             hindi_output_syllab[i]="1"
        if(hindi_output_syllab[i]=="&"): 
             hindi_output_syllab[i]="1"
  hindi_output_syllab="".join(hindi_output_syllab)
  hindi_output_syllab=hindi_output_syllab.replace("0",") (0 ")
  hindi_output_syllab=hindi_output_syllab.replace("1",") (1 ")
  #hindi_output_syllab=hindi_output_syllab.replace("",") (1 ")
  print "checking", hindi_output_syllab[0]
  if hindi_output_syllab[0]==")":
   hindi_output_syllab=hindi_output_syllab[1:]
   hindi_output_syllab=hindi_output_syllab+")"
  entries['Phoneme Level(ASCII)'].delete(0,END)
  entries['Phoneme Level(ASCII)'].insert(0,hindi_output_syllab)
  

  
  for i in range(len(hindi_output1)):
	  if(hindi_output1[i]=="$"):
	     count_final_strong_syll=count_final_strong_syll+1
	     final_strong_syll.append(i)
  print final_strong_syll
  print count_final_strong_syll
  if (count_weak_syllable+count_strong_syllable+count_superstrong_syllable==2):
    for i in range(len(hindi_output1)):
      if(hindi_output1[i]=="@"):
	hindi_output1[i]="'"
      elif((hindi_output1[i]=="$" or hindi_output1[i]=="&")):
        hindi_output1[i]="'"
      
        
    #LabelConverter(entries)
    #print hindi_output_syllab
    hindi_output_syllab=''.join(hindi_output1)
    hindi_output_syllab=hindi_output_syllab.replace("@",u'\u03c3\u02b7')
    hindi_output_syllab=hindi_output_syllab.replace("$",u'\u03c3\u02b0')
    hindi_output_syllab=hindi_output_syllab.replace("&",u'\u03c3\u02e2\u02b0')
    hindi_output_syllab=hindi_output_syllab.replace("*",u'<\u03c3\u02e2>')
    hindi_output_syllab=Labelchanger2(hindi_output_syllab)
    
    entries['Phoneme Level(ASCII)'].delete(0,END)
    entries['Phoneme Level(ASCII)'].insert(0,hindi_output_syllab)
  #countlabel=0
  #for i in range(len(hindi_output1)):
    
    #if(hindi_output1[i]=="@" or hindi_output1[i]=="$" or hindi_output1[i]=="&"):
      # countlabel+=1
  #print "countlabel",countlabel

  for i in range (len(hindi_output1)):
        if((hindi_output1[i]=="$" and i!=final_strong_syll[len(final_strong_syll)-1])  or hindi_output1[i]=="&"):
	     hindi_output1[i]="'" 
        if(countlabel==2):
         if(i+2!=""):
          if(hindi_output1[i]=="@" and hindi_output1[i+2]=="$" ):
             print"aao2"
             hindi_output1[i]="'"
	  elif(hindi_output1[i]=="@"):
	     hindi_output1[i]=""
          if(hindi_output1[i]=="$" and hindi_output1[i+2]=="$" ): 
             hindi_output1[i]="'"
          elif(hindi_output1[i]=="$"):
             hindi_output1[i]=""
        if(countlabel==2):
         if(i+3!=""):
          if(hindi_output1[i]=="@" and hindi_output1[i+3]=="$" ):
             print"aao2"
             hindi_output1[i]="'"
	  elif(hindi_output1[i]=="@"):
	     hindi_output1[i]=""
          if(hindi_output1[i]=="$" and  hindi_output1[i+3]=="&" ): 
             hindi_output1[i]="'"
          elif(hindi_output1[i]=="$"):
             hindi_output1[i]=""
        if(countlabel>=3):
  
          if(hindi_output1[i]=="$" and (hindi_output1[i+2]=="$" or hindi_output1[i+2]=="@" or hindi_output1[i+2]=="&")):
             hindi_output1[i]="'"
          elif(hindi_output1[i]=="$"): 
             hindi_output1[i]=""
          if(hindi_output1[i]=="@"): 
             hindi_output1[i]=""
        if(countlabel>=3):
         if(i+3!=""): 
          if(hindi_output1[i]=="$" and (hindi_output1[i+3]=="$" or hindi_output1[i+3]=="@" or hindi_output1[i+3]=="&")):
             hindi_output1[i]="'"
          elif(hindi_output1[i]=="$"): 
             hindi_output1[i]=""
          if(hindi_output1[i]=="@"): 
             hindi_output1[i]=""
        if(hindi_output1[i]=="&"): 
             hindi_output1[i]="'"
      
    
  hindi_output_syllab=""
  hindi_output_syllab=''.join(hindi_output1)
  hindi_output_syllab=hindi_output_syllab.replace("@",u'\u03c3\u02b7')
  hindi_output_syllab=hindi_output_syllab.replace("$",u'\u03c3\u02b0')
  hindi_output_syllab=hindi_output_syllab.replace("&",u'\u03c3\u02e2\u02b0')
  hindi_output_syllab=hindi_output_syllab.replace("*",u'<\u03c3\u02e2>')
  hindi_output_syllab=Labelchanger2(hindi_output_syllab)
  print hindi_output_syllab
   
  entries['Phoneme Level(IPA)'].delete(0,END)
  entries['Phoneme Level(IPA)'].insert(0,hindi_output_syllab)

  
