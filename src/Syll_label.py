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

reload(sys)
sys.setdefaultencoding('utf-8')
from countvc import countvowel

uvwl1 = [u'\u0259', "u", "E", "A", "O", "M", "J", "N", u'i', u'a', "U", "I", u'!', u'#', u'%', u'(', u')',
         u'_', u'+', u'=', u'1', u'`']
long_vowel = ["E", "A", "O", "M", "J", "N", "U", "I"]
short_vowel = ["i", "o", "u", u'\u0259']
uc = [u'p', u'b', u't', u'd', u'\u0288', u'\u0256', u't\u0283', u'd\u0292', u'k', u'g', u'q', u'm', u'n', u'\u0273',
      u'f', u's', u'z', u'\u0283', u'x', u'\u0263', u'h', u'\u028b', u'j', u'r', u'l', u'\u023f', u'\u027d', u'\u0272',
      u'\u014b']
ucp = ["P", "B", "T", "D", "Q", "C", "c", "Z", "5", "K", "R", "G"]
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
countweight = 0
global hindi_output
hindi_output = []
global hindi_output1
hindi_output1 = []


def Labeling(entries):
    Syllabify(entries)
    hindi_output = (entries['I-Level Syllabification'].get()).rstrip()
    hindi_output2=Labelchanger1(hindi_output)
    hindi_output1=list(hindi_output2)
    indexvowelsnew=[]
    newvowelindexes=[]
    countv, countc = countvowel(hindi_output1)
    if (countv == 1):

        entries['Prosodic Label(PLSB)'].delete(0, END)
        entries['Prosodic Label(PLSB)'].insert(0, hindi_output)

    else:
        newvowelindexes = list(set(hindi_output1) & set(uvwl1))

        for k in range(len(newvowelindexes)):
            for j in range(len(hindi_output1)):
                if (newvowelindexes[k] == hindi_output1[j]):
                    indexvowelsnew.append(j)
                    indexvowelsnew.sort()
        countweight = []
        for k in range(len(indexvowelsnew)):
            for j in range(len(short_vowel)):
                if (hindi_output1[indexvowelsnew[k]] == short_vowel[j]):
                    countweight.append(1)

            for j in range(len(long_vowel)):
                if (hindi_output1[indexvowelsnew[k]] == long_vowel[j]):
                    countweight.append(2)

        newpos = []
        for i in range(len(hindi_output1)):
            if hindi_output1[i] == ".":
                newpos.append(i)
        
    for i in range(len(indexvowelsnew) - 1):
        if newpos[i] - indexvowelsnew[i] == 1 and countweight[i] == 1 and i == 0:
            hindi_output1.insert(0, "@")
        if newpos[i] - indexvowelsnew[i] == 1 and countweight[i] == 2 and i == 0:
            hindi_output1.insert(0, "$")
        if newpos[i] - indexvowelsnew[i] == 2 and countweight[i] == 1 and i == 0:
            hindi_output1.insert(0, "$")
        if newpos[i] - indexvowelsnew[i] >= 3 and countweight[i] == 1 and i == 0:
            hindi_output1.insert(0, "&")
        if newpos[i] - indexvowelsnew[i] >= 2 and countweight[i] == 2 and i == 0:
            hindi_output1.insert(0, "&")
        if newpos[i] - indexvowelsnew[i] == 1 and countweight[i] == 1 and i == 1:
            hindi_output1[newpos[i - 1]] = "@"
        if newpos[i] - indexvowelsnew[i] == 1 and countweight[i] == 2 and i == 1:
            hindi_output1[newpos[i - 1]] = "$"
        if newpos[i] - indexvowelsnew[i] == 2 and countweight[i] == 1 and i == 1:
            hindi_output1[newpos[i - 1]] = "$"
        if newpos[i] - indexvowelsnew[i] >= 3 and countweight[i] == 1 and i == 1:
            hindi_output1[newpos[i - 1]] = "&"
        if newpos[i] - indexvowelsnew[i] >= 2 and countweight[i] == 2 and i == 1:
            hindi_output1[newpos[i - 1]] = "&"
        if newpos[i] - indexvowelsnew[i] == 1 and countweight[i] == 1 and i >= 2:
            hindi_output1[indexvowelsnew[i] - 1] = "@"
        if newpos[i] - indexvowelsnew[i] == 1 and countweight[i] == 2 and i >= 2:
            hindi_output1[indexvowelsnew[i] - 1] = "$"
        if newpos[i] - indexvowelsnew[i] == 2 and countweight[i] == 1 and i >= 2:
            hindi_output1[indexvowelsnew[i] - 1] = "$"
        if newpos[i] - indexvowelsnew[i] >= 3 and countweight[i] == 1 and i >= 2:
            hindi_output1[indexvowelsnew[i] - 1] = "&"
        if newpos[i] - indexvowelsnew[i] >= 2 and countweight[i] == 2 and i >= 2:
            hindi_output1[indexvowelsnew[i] - 1] = "&"
        newpos[i] += i + 1
        indexvowelsnew[i] += i + 1

        if countweight[len(countweight) - 1] == 1:
            if hindi_output1[indexvowelsnew[len(indexvowelsnew) - 1] - 1] == ".":
                hindi_output1[indexvowelsnew[len(indexvowelsnew) - 1] - 1] = "$"
            elif hindi_output1[indexvowelsnew[len(indexvowelsnew) - 1]] == ".":
                hindi_output1[indexvowelsnew[len(indexvowelsnew) - 1]] = "$"
                # print hindi_output1[indexvowelsnew[len(indexvowelsnew)-1]+1]
        if (countweight[len(countweight) - 1] == 2 and len(hindi_output1) > indexvowelsnew[
                len(indexvowelsnew) - 1] + 2 and hindi_output1[len(hindi_output1) - 1] != "X"):
            if hindi_output1[indexvowelsnew[len(indexvowelsnew) - 1] - 1] == ".":
                hindi_output1[indexvowelsnew[len(indexvowelsnew) - 1] - 1] = "&"
            elif hindi_output1[indexvowelsnew[len(indexvowelsnew) - 1]] == ".":
                hindi_output1[indexvowelsnew[len(indexvowelsnew) - 1]] = "&"
        else:
            if (hindi_output1[indexvowelsnew[len(indexvowelsnew) - 1] - 2] == "."):
                hindi_output1[indexvowelsnew[len(indexvowelsnew) - 1] - 2] = "$"
            if (hindi_output1[indexvowelsnew[len(indexvowelsnew) - 1] - 1] == "."):
                hindi_output1[indexvowelsnew[len(indexvowelsnew) - 1] - 1] = "$"
            elif (hindi_output1[indexvowelsnew[len(indexvowelsnew) - 1]] == "."):
                hindi_output1[indexvowelsnew[len(indexvowelsnew) - 1]] = "$"
    labelpos = []
    for i in range(len(hindi_output1)):
        if (hindi_output1[i] == "@" or hindi_output1[i] == "$" or hindi_output1[i] == "*" or hindi_output1[i] == "&"):
            labelpos.append(i)
            # ******************** Relabeling and Internal Deletion *************************************
    if ((len(indexvowelsnew) <= 3 or (hindi_output1[len(hindi_output1) - 2] == "t" and (
                                hindi_output1[len(hindi_output1) - 1] == "A" or hindi_output1[
                                len(hindi_output1) - 1] == "I" or
                            hindi_output1[len(hindi_output1) - 1] == "O" or hindi_output1[
                        len(hindi_output1) - 1] == "U" or
                    hindi_output1[len(hindi_output1) - 1] == "E")) or hindi_output1[len(labelpos) - 1] == "&") or (
                        len(indexvowelsnew) <= 3 or (hindi_output1[len(hindi_output1) - 3] == "t" and (
                                            hindi_output1[len(hindi_output1) - 2] == "A" or hindi_output1[
                                            len(hindi_output1) - 2] == "I" or hindi_output1[
                                        len(hindi_output1) - 2] == "O" or
                                    hindi_output1[len(hindi_output1) - 2] == "U" or hindi_output1[
                                len(hindi_output1) - 2] == "E") and
                                                             hindi_output1[len(hindi_output1) - 1] == "X") or
                    hindi_output1[
                            len(labelpos) - 1] == "&")):
        for i in reversed(range(1, len(labelpos) - 1)):

            if (hindi_output1[labelpos[i - 1]] == "@" and hindi_output1[labelpos[i]] == "@"):
                hindi_output1[labelpos[i - 1]] = "$"
            if (hindi_output1[labelpos[i - 1]] == "$" and hindi_output1[labelpos[i]] == "$"):
                hindi_output1[labelpos[i - 1]] = "@"
            if (hindi_output1[labelpos[i - 1]] == "$" and hindi_output1[labelpos[i]] == "&"):
                hindi_output1[labelpos[i - 1]] = "@"


                #  ***** Schwa Deletion1******

            if (hindi_output1[labelpos[i - 1]] == "$" and hindi_output1[labelpos[i]] == "@"):
                if (hindi_output1[labelpos[i] + 1] == u'\u0259'):
                    hindi_output1[labelpos[i] + 1] = ""
                    hindi_output1[labelpos[i]] = ""
                    hindi_output1[labelpos[i - 1]] = "&"
                if (hindi_output1[labelpos[i] + 2] == u'\u0259'):
                    hindi_output1[labelpos[i] + 2] = ""
                    hindi_output1[labelpos[i]] = ""
                    hindi_output1[labelpos[i - 1]] = "&"
            if (hindi_output1[labelpos[i - 1]] == "&" and hindi_output1[labelpos[i]] == "@"):
                if (hindi_output1[labelpos[i] + 1] == u'\u0259'):
                    hindi_output1[labelpos[i] + 1] = ""
                    hindi_output1[labelpos[i]] = ""
                if (hindi_output1[labelpos[i] + 2] == u'\u0259'):
                    hindi_output1[labelpos[i] + 2] = ""
                    hindi_output1[labelpos[i]] = ""

                    # ******** For for compound words without "ta:" symbols in the end or a superheavy syllable in the end ***************************

    else:
        for i in reversed(range(1, len(labelpos) - 2)):
            if (hindi_output1[labelpos[i - 1]] == "@" and hindi_output1[labelpos[i]] == "@"):
                hindi_output1[labelpos[i - 1]] = "$"
            if (hindi_output1[labelpos[i - 1]] == "$" and hindi_output1[labelpos[i]] == "$"):
                hindi_output1[labelpos[i - 1]] = "@"
            if (hindi_output1[labelpos[i - 1]] == "$" and hindi_output1[labelpos[i]] == "&"):
                hindi_output1[labelpos[i - 1]] = "@"

                #  ***** Schwa Deletion2******

            if (hindi_output1[labelpos[i - 1]] == "$" and hindi_output1[labelpos[i]] == "@"):
                if (hindi_output1[labelpos[i] + 1] == u'\u0259'):
                    hindi_output1[labelpos[i] + 1] = ""
                    hindi_output1[labelpos[i]] = ""
                    hindi_output1[labelpos[i - 1]] = "&"
                if (hindi_output1[labelpos[i] + 2] == u'\u0259'):
                    hindi_output1[labelpos[i] + 2] = ""
                    hindi_output1[labelpos[i]] = ""
                    hindi_output1[labelpos[i - 1]] = "&"
            if (hindi_output1[labelpos[i - 1]] == "&" and hindi_output1[labelpos[i]] == "@"):
                if (hindi_output1[labelpos[i] + 1] == u'\u0259'):
                    hindi_output1[labelpos[i] + 1] = ""
                    hindi_output1[labelpos[i]] = ""
                if (hindi_output1[labelpos[i] + 2] == u'\u0259'):
                    hindi_output1[labelpos[i] + 2] = ""
                    hindi_output1[labelpos[i]] = ""

                    # ****** Anusvara Anunashika disambiguation ************************
    hindi_output1 = filter(bool, hindi_output1)
    labelvowelindexes = list(set(hindi_output1) & set(uvwl1))
    labelindexvowels = []
    for k in range(len(labelvowelindexes)):
        for j in range(len(hindi_output1)):
            if (labelvowelindexes[k] == hindi_output1[j]):
                labelindexvowels.append(j)
                labelindexvowels.sort()
        labelcountweight = []
        for k in range(len(labelindexvowels)):
            for j in range(len(short_vowel)):
                if (hindi_output1[labelindexvowels[k]] == short_vowel[j]):
                    labelcountweight.append(1)

            for j in range(len(long_vowel)):
                if (hindi_output1[labelindexvowels[k]] == long_vowel[j]):
                    labelcountweight.append(2)
    labelnewpos = []
    for i in range(len(hindi_output1)):
        if hindi_output1[i] == "$" or hindi_output1[i] == "@" or hindi_output1[i] == "*" or hindi_output1[i] == "&":
            labelnewpos.append(i)
    
    for i in range(len(labelnewpos) - 1):
        if (labelnewpos[i + 1] - labelindexvowels[i] == 2):
            labelcountweight[i] += 1

        if (labelnewpos[i + 1] - labelindexvowels[i] >= 3):
            labelcountweight[i] += 2
     
    if (len(hindi_output1) == labelindexvowels[len(labelindexvowels) - 1] + 2):
        labelcountweight[len(labelcountweight) - 1] += 1
    if (len(hindi_output1) >= labelindexvowels[len(labelindexvowels) - 1] + 3):
        labelcountweight[len(labelcountweight) - 1] += 2
    c_class = ["c", "C", "5", "Z"]
    p_class = ["p", "P", "b", "B"]
    t_class = ["t", "T", "d", "D"]
    k_class = ["k", "K", "g", "G"]
    T_class = [u'\u0256', "Q", u'\u0288', u'\u02b1']
    O_class = ["c", "C", "5", "Z", "p", "P", "b", "B", "t", "T", "d", "D", u'\u0256', "Q", u'\u0288', u'\u02b1']
    if len(labelcountweight) > len(labelnewpos):
        for i in range(len(labelcountweight) - 2):
            if (labelcountweight[i] <= labelcountweight[i + 1]):
                for j in range(labelnewpos[i], labelnewpos[i] + 4):
                    if (hindi_output1[j] == "X"):
                        k = j
                    for p in range(4):
                        if (hindi_output1[k] == "X" and (
                                        hindi_output1[k + 1] == p_class[p] or hindi_output1[k + 1] == u'\u028b')):
                           
                            hindi_output1[k] = "m"
                        if (hindi_output1[k] == "X" and (
                                        hindi_output1[k + 2] == p_class[p] or hindi_output1[k + 2] == u'\u028b')):
                            
                            hindi_output1[k] = "m"
                        if (hindi_output1[k] == "X" and hindi_output1[k + 1] == t_class[p]):
                            
                            hindi_output1[k] = "n"
                        if (hindi_output1[k] == "X" and hindi_output1[k + 2] == t_class[p]):
                            
                            hindi_output1[k] = "n"
                        if (hindi_output1[k] == "X" and hindi_output1[k + 1] == k_class[p]):
                            
                            hindi_output1[k] = u'\u014b'
                        if (hindi_output1[k] == "X" and hindi_output1[k + 2] == k_class[p]):
                            
                            hindi_output1[k] = u'\u014b'
                        if (hindi_output1[k] == "X" and hindi_output1[k + 1] == c_class[p]):
                            
                            hindi_output1[k] = "n"
                        if (hindi_output1[k] == "X" and hindi_output1[k + 2] == c_class[p]):
                            
                            hindi_output1[k] = "n"
                        if (hindi_output1[k] == "X" and hindi_output1[k + 1] == T_class[p]):
                            
                            hindi_output1[k] = "n"
                        if (hindi_output1[k] == "X" and hindi_output1[k + 2] == T_class[p]):
                           
                            hindi_output1[k] = "n"
                        if (hindi_output1[k] == "X" and (hindi_output1[k + 1] == "s" or hindi_output1[k + 1] == "S")):
                            
                            hindi_output1[k] = "n"
                        if (hindi_output1[k] == "X" and (hindi_output1[k + 2] == "s" or hindi_output1[k + 2] == "S")):
                            
                            hindi_output1[k] = "n"

    else:
        for i in range(len(labelcountweight) - 1):
            # *********Homo-organic Nasal**********************************
            if (labelcountweight[i] <= labelcountweight[i + 1]):
               
                # print "labelnewpos[i+1]",labelnewpos[i+1]

                for j in range(labelnewpos[i], labelnewpos[i] + 4):
                    if (hindi_output1[j] == "X"):
                        
                        k = j
                    for p in range(4):
                        if (hindi_output1[k] == "X" and (
                                        hindi_output1[k + 1] == p_class[p] or hindi_output1[k + 1] == u'\u028b')):
                            
                            hindi_output1[k] = "m"
                        if (hindi_output1[k] == "X" and (
                                        hindi_output1[k + 2] == p_class[p] or hindi_output1[k + 2] == u'\u028b')):
                            
                            hindi_output1[k] = "m"
                        if (hindi_output1[k] == "X" and hindi_output1[k + 1] == t_class[p]):
                            
                            hindi_output1[k] = "n"
                        if (hindi_output1[k] == "X" and hindi_output1[k + 2] == t_class[p]):
                            
                            hindi_output1[k] = "n"
                        if (hindi_output1[k] == "X" and hindi_output1[k + 1] == k_class[p]):
                            
                            hindi_output1[k] = u'\u014b'
                        if (hindi_output1[k] == "X" and hindi_output1[k + 2] == k_class[p]):
                            
                            hindi_output1[k] = u'\u014b'
                        if (hindi_output1[k] == "X" and hindi_output1[k + 1] == c_class[p]):
                            
                            hindi_output1[k] = "n"
                        if (hindi_output1[k] == "X" and hindi_output1[k + 2] == c_class[p]):
                            
                            hindi_output1[k] = "n"
                        if (hindi_output1[k] == "X" and hindi_output1[k + 1] == T_class[p]):
                            
                            hindi_output1[k] = "n"
                        if (hindi_output1[k] == "X" and hindi_output1[k + 2] == T_class[p]):
                            
                            hindi_output1[k] = "n"
                        if (hindi_output1[k] == "X" and (hindi_output1[k + 1] == "s" or hindi_output1[k + 1] == "S")):
                            
                            hindi_output1[k] = "n"
                        if (hindi_output1[k] == "X" and (hindi_output1[k + 2] == "s" or hindi_output1[k + 2] == "S")):
                            
                            hindi_output1[k] = "n"


                            # ********* Nasalized Vowel ******************************************************
    if (countv > 1):
        if len(labelcountweight) > len(newpos):
            for i in range(len(labelcountweight) - 1):
                if (labelcountweight[i] > labelcountweight[i + 1]):
                  
                    for j in range(labelnewpos[i], labelnewpos[i] + 4):
                        if (hindi_output1[j] == "X"):
                            k = j - 1

                        if (hindi_output1[k] == "E" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "_"
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "A" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "="
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "O" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "7"
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "I" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "#"
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "U" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "("
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "J" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "+"
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "N" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = ")"
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "i" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "!"
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "u" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "%"
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == u'\u0259' and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "`"
                            hindi_output1[k + 1] = ""

        else:
            for i in range(len(labelcountweight) - 1):
                if (labelcountweight[i] > labelcountweight[i + 1]):
                    
                    for j in range(labelnewpos[i], labelnewpos[i] + 4):
                        if (hindi_output1[j] == "X"):
                            k = j - 1

                        if (hindi_output1[k] == "E" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "_"
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "A" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "="
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "O" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "7"
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "I" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "#"
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "U" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "("
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "J" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "+"
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "N" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = ")"
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "i" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "!"
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == "u" and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "%"
                            hindi_output1[k + 1] = ""
                        if (hindi_output1[k] == u'\u0259' and hindi_output1[k + 1] == "X"):
                            hindi_output1[k] = "`"
                            hindi_output1[k + 1] = ""

    hindi_output1 = filter(bool, hindi_output1)
    
    if (countv > 1):
        for i in range(4):
            if (hindi_output1[len(hindi_output1) - 2] == "X" and hindi_output1[len(hindi_output1) - 1] == k_class[i]):
                hindi_output1[len(hindi_output1) - 2] = u'\u014b'
            if (hindi_output1[len(hindi_output1) - 2] == "X" and (
                            hindi_output1[len(hindi_output1) - 1] == p_class[i] or hindi_output1[
                            len(hindi_output1) - 1] == u'\u028b')):
                hindi_output1[len(hindi_output1) - 2] = "m"
                flag = 1
            if (hindi_output1[len(hindi_output1) - 2] == "X" and hindi_output1[len(hindi_output1) - 1] == t_class[i]):
                hindi_output1[len(hindi_output1) - 2] = "n"
                flag = 1
            if (hindi_output1[len(hindi_output1) - 2] == "X" and hindi_output1[len(hindi_output1) - 1] == T_class[i]):
                hindi_output1[len(hindi_output1) - 2] = "n"





              
    else:
        
        for k in range(len(hindi_output1) - 2):
            
            for j in range(4):
                if (hindi_output1[k] == "E" and hindi_output1[k + 1] == "X" and hindi_output1[k + 2] == c_class[j]):
                    hindi_output1[k] = "_"
                    hindi_output1[k + 1] = ""
                if (hindi_output1[k] == "A" and hindi_output1[k + 1] == "X" and hindi_output1[k + 2] == c_class[j]):
                    hindi_output1[k] = "="
                    hindi_output1[k + 1] = ""
                    
                if (hindi_output1[k] == "O" and hindi_output1[k + 1] == "X" and hindi_output1[k + 2] == c_class[j]):
                    hindi_output1[k] = "7"
                    hindi_output1[k + 1] = ""
                if (hindi_output1[k] == "I" and hindi_output1[k + 1] == "X" and hindi_output1[k + 2] == c_class[j]):
                    hindi_output1[k] = "#"
                    hindi_output1[k + 1] = ""
                if (hindi_output1[k] == "U" and hindi_output1[k + 1] == "X" and hindi_output1[k + 2] == c_class[j]):
                    hindi_output1[k] = "("
                    hindi_output1[k + 1] = ""
                if (hindi_output1[k] == "J" and hindi_output1[k + 1] == "X" and hindi_output1[k + 2] == c_class[j]):
                    hindi_output1[k] = "+"
                    hindi_output1[k + 1] = ""
                if (hindi_output1[k] == "N" and hindi_output1[k + 1] == "X" and hindi_output1[k + 2] == c_class[j]):
                    hindi_output1[k] = ")"
                    hindi_output1[k + 1] = ""
                if (hindi_output1[k] == "i" and hindi_output1[k + 1] == "X" and hindi_output1[k + 2] == c_class[j]):
                    hindi_output1[k] = "!"
                    hindi_output1[k + 1] = ""
                if (hindi_output1[k] == "u" and hindi_output1[k + 1] == "X" and hindi_output1[k + 2] == c_class[j]):
                    hindi_output1[k] = "%"
                    hindi_output1[k + 1] = ""
                    
        for k in range(len(hindi_output1) - 1):
            for j in range(4):
                if (hindi_output1[k] == "X" and hindi_output1[k + 1] == k_class[j]):
                    hindi_output1[k] = u'\u014b'
                if (hindi_output1[k] == "X" and (
                                hindi_output1[k + 1] == p_class[j] or hindi_output1[k + 1] == u'\u028b')):
                    hindi_output1[k] = "m"
                if (hindi_output1[k] == "X" and hindi_output1[k + 1] == t_class[j]):
                    hindi_output1[k] = "n"
                if (hindi_output1[k] == "X" and hindi_output1[k + 1] == T_class[j]):
                    hindi_output1[k] = "n"
                if (hindi_output1[k] == "X" and hindi_output1[k + 1] != O_class[j]):
                    hindi_output1[k] = "n"



                    
    if (hindi_output1[len(hindi_output1) - 2] == "E" and hindi_output1[len(hindi_output1) - 1] == "X"):
        hindi_output1[len(hindi_output1) - 2] = "_"
        hindi_output1[len(hindi_output1) - 1] = ""
    if (hindi_output1[len(hindi_output1) - 2] == "A" and hindi_output1[len(hindi_output1) - 1] == "X"):
        hindi_output1[len(hindi_output1) - 2] = "="
        hindi_output1[len(hindi_output1) - 1] = ""
    if (hindi_output1[len(hindi_output1) - 2] == "O" and hindi_output1[len(hindi_output1) - 1] == "X"):
        hindi_output1[len(hindi_output1) - 2] = "7"
        hindi_output1[len(hindi_output1) - 1] = ""
    if (hindi_output1[len(hindi_output1) - 2] == "I" and hindi_output1[len(hindi_output1) - 1] == "X"):
        hindi_output1[len(hindi_output1) - 2] = "#"
        hindi_output1[len(hindi_output1) - 1] = ""
    if (hindi_output1[len(hindi_output1) - 2] == "U" and hindi_output1[len(hindi_output1) - 1] == "X"):
        hindi_output1[len(hindi_output1) - 2] = "("
        hindi_output1[len(hindi_output1) - 1] = ""
    if (hindi_output1[len(hindi_output1) - 2] == "J" and hindi_output1[len(hindi_output1) - 1] == "X"):
        hindi_output1[len(hindi_output1) - 2] = "+"
        hindi_output1[len(hindi_output1) - 1] = ""
    if (hindi_output1[len(hindi_output1) - 2] == "N" and hindi_output1[len(hindi_output1) - 1] == "X"):
        hindi_output1[len(hindi_output1) - 2] = ")"
        hindi_output1[len(hindi_output1) - 1] = ""
   
    hindi_output_syllab = ''.join(hindi_output1)
    hindi_output_syllab = hindi_output_syllab.replace("@", u'\u03c3\u02b7')
    hindi_output_syllab = hindi_output_syllab.replace("$", u'\u03c3\u02b0')
    hindi_output_syllab = hindi_output_syllab.replace("&", u'\u03c3\u02e2\u02b0')
    hindi_output_syllab = hindi_output_syllab.replace("*", u'<\u03c3\u02e2>')
    hindi_output_syllab = Labelchanger2(hindi_output_syllab)
    entries['Prosodic Label(PLSB)'].delete(0, END)
    entries['Prosodic Label(PLSB)'].insert(0, hindi_output_syllab)
