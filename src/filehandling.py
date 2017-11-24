from Tkinter import *
from itertools import groupby
import tkFileDialog
import codecs
import sys
import re
import os
import xlsxwriter
import subprocess
import xlrd
import tkFont
reload(sys)
from IPAEquv import IPAEquivalent
from Labelchang1 import Labelchanger1
from Labelchang2 import Labelchanger2
from Syllabification import Syllabify
from Syll_label import Labeling
from phoneme import Phoneme
reload(sys)
sys.setdefaultencoding('utf-8')
def load_file(entries):
  fileinput=open(tkFileDialog.askopenfilename(),'r')
  print fileinput
  path=os.getcwd()
  print "path=",path
  fileoutput=open(path+"/"+"PLS_XML_W3C_Format_Lexicon.txt", 'aw')
  fileoutput1=open(path+"/"+"PLS_Festival_Format_Lexicon.txt", 'aw')
  
  for word in fileinput:
           hindi_input=word.rstrip()
           print hindi_input
           entries['Hindi Input'].delete(0,END)
           entries['Hindi Input'].insert(0,word)
           Phoneme(entries)
           fileoutput.write("<lexeme>\n")
           fileoutput.write("<Grapheme>"+(word).rstrip()+"</Grapheme>"+"\n"+"<PS>"+ entries['Prosodic Label(PLSB)'].get() +"</PS>"+'\n'+ "<Phoneme>"+entries['Phoneme Level(IPA)'].get()+"</Phoneme>"+'\n' )
           fileoutput.write("</lexeme>\n")
       
           fileoutput1.write("( "+(word).rstrip()+"\t"+entries['Phoneme Level(ASCII)'].get()+" )\n" )
           subprocess.call(["sed -i 's/\\\t)//g'",path+"/"+"PLS_Festival_Format_Lexicon.txt"], shell=True)
