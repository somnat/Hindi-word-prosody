from Tkinter import *
from itertools import groupby
import tkFileDialog
import codecs
import sys
import re
import os
import xlrd
import tkFont
import xlsxwriter
import subprocess
reload(sys)
sys.setdefaultencoding('utf-8')

#from input import makeform
ucv = [u'\u092a', u'\u092c', u'\u092b', u'\u092d', u'\u0924', u'\u0926', u'\u0925', u'\u0927', u'\u091f', u'\u0921',
       u'\u0920', u'\u0922', u'\u091a', u'\u091c', u'\u091b', u'\u091d', u'\u0915', u'\u0916', u'\u0917', u'\u0918',
       u'\u0958', u'\u092e', u'\u0928', u'\u0923', u'\u095e', u'\u0938', u'\u095b', u'\u0936', u'\u0959', u'\u095a',
       u'\u0939', u'\u0935', u'\u092f', u'\u0930', u'\u0932', u'\u0907', u'\u0905', u'\u0909', u'\u0908', u'\u090f',
       u'\u0906', u'\u0913', u'\u0911', u'\u090a', u'\u0910', u'\u0914', u'\u090b', u'\u093f', u'\u093c', u'\u0941',
       u'\u0940', u'\u0947', u'\u093e', u'\u094b', u'\u0949', u'\u0942', u'\u0948', u'\u094c', u'\u0937', u'\u095c',
       u'\u091e', u'\u095d', u'\u0919', u'\u0902', u'\u0901', u'-', u' ']

# IPA unicode strings
uipa = [u'p\u0259', u'b\u0259', u'p\u02b0\u0259', u'b\u02b1\u0259', u't\u0259', u'd\u0259', u't\u02b0\u0259',
        u'd\u02b1\u0259', u'\u0288\u0259', u'\u0256\u0259', u'\u0288\u02b0\u0259', u'\u0256\u02b1\u0259',
        u't\u0283\u0259', u'd\u0292\u0259', u't\u0283\u02b0\u0259', u'd\u0292\u02b1\u0259', u'k\u0259',
        u'k\u02b0\u0259', u'g\u0259', u'\u0261\u02b1\u0259', u'q\u0259', u'm\u0259', u'n\u0259', u'\u0273\u0259',
        u'f\u0259', u's\u0259', u'z\u0259', u'\u0283\u0259', u'x\u0259', u'\u0263\u0259', u'h\u0259', u'\u028b\u0259',
        u'j\u0259', u'r\u0259', u'l\u0259', u'2', u'\u0259', u'u', u'3', u'4', u'a:', u'o:', u'\u0254:', u'u:',
        u'\xe6:', u'\u1d14:', u'ri', u'i', u'\u0259', u'u', u'i:', u'e:', u'a:', u'o:', u'\u0254:', u'u:', u'\xe6:',
        u'\u1d14:', u'\u023f\u0259', u'\u027d\u0259', u'\u0272\u0259', u'\u027d\u02b1\u0259', u'\u014b\u0259', "^", "~",
        u'-', u' ']

uc = [u'p', u'b', u't', u'd', u'\u0288', u'\u0256', u't\u0283', u'd\u0292', u'k', u'g', u'q', u'm', u'n', u'\u0273',
      u'f', u's', u'z', u'\u0283', u'x', u'\u0263', u'h', u'\u028b', u'j', u'r', u'l', u'\u023f', u'\u027d', u'\u0272',
      u'\u014b']

ustop = [u'p', u'b', u't', u'k', u'd', u'g', u'P', u'K', u'G', u'D']

# Array for plosive and and other containing more than one unicode symbols

ucp = ["P", "B", "T", "D", "Q", "C", "c", "Z", "5", "K", "R", "G"]

# print len(ucv)
# print len(uipa)
# Hindi Vowels in IPA
uvwl = {u'\u0259': 0, u'u': 0, u'E': 0, u'M': 0, u'A': 0, u'O': 0, u'\u0254': 0, "J": 0, "N": 0, u'i': 0, u'a': 0,
        u'U': 0, u'I': 0, u'!': 0, u'#': 0, u'%': 0, u'(': 0, u')': 0, u'_': 0, u'+': 0, u'=': 0, u'1': 0, u'`': 0}
uvwl1 = [u'\u0259', "u", "E", "A", "O", "M", "J", "N", u'i', u'a', "U", u'\u0254', "I", u'!', u'#', u'%', u'(', u')',
         u'_', u'+', u'=', u'1', u'`']
long_vowel = ["E", "A", "O", "M", "J", "N", "U", "I"]
short_vowel = ["i", "o", "u", u'\u0259']

def IPAEquivalent(entries):

    global hindi_output
    hindi_output = ""
    hindi_input = []

    ############################ Input from a file ##################################################################################


    hindi_input_new = (entries['Hindi Input'].get())
    hindi_input_array = hindi_input_new.split()
    for word in hindi_input_array:
        hindi_input = word
        length = len(hindi_input)
        for i in range((len(hindi_input))):
            for j in range(len(ucv)):
                if ((hindi_input[i] == ucv[j] and i != length - 1) and (hindi_input[i + 1] == u'\u094d')):  # for halant
                    temp = uipa[j].replace(u'\u0259', "")
                    hindi_output = hindi_output + temp
                    i = i + 1

                if ((hindi_input[i] == ucv[j] and i != length - 1) and (hindi_input[i + 1] == u'\u0943')):  # for ri
                    temp = uipa[j].replace(u'\u0259', "")
                    hindi_output = hindi_output + temp + "ri"
                    i = i + 1

                if ((hindi_input[i] == ucv[j] and i != length - 1) and (
                        hindi_input[i + 1] == u'\u0903' and i + 1 == length - 1)):  # for visarg
                    temp = uipa[j]
                    hindi_output = hindi_output + temp + "h"
                    i = i + 1

                    # replacing schwa before vowels
                if (hindi_input[i] == ucv[j]):
                    hindi_output = hindi_output + (uipa[j])
                    hindi_output = hindi_output.replace(u'\u0259u', "u")
                    hindi_output = hindi_output.replace(u'\u0259i', "i")
                    hindi_output = hindi_output.replace(u'\u0259i:', "i:")
                    hindi_output = hindi_output.replace(u'\u0259o:', "o:")
                    hindi_output = hindi_output.replace(u'\u0259a:', "a:")
                    hindi_output = hindi_output.replace(u'\u0259e:', "e:")
                    hindi_output = hindi_output.replace(u'\u0259e:', "e:")
                    hindi_output = hindi_output.replace(u'\u0259\u0254:', u'\u0254:')
                    hindi_output = hindi_output.replace(u'\u0259\xe6:', u'\xe6:')
                    # hindi_output=hindi_output.replace(u'\u0259\u1d14:','u\u1d14:')
                    hindi_output = hindi_output.replace(u'3', "i:")
                    hindi_output = hindi_output.replace(u'2', "i")
                    hindi_output = hindi_output.replace(u'4', "e:")
        hindi_output_ipa = []
        hindi_output_ipa = list(hindi_output)
        for i in range(1, len(hindi_output_ipa)):
            if (hindi_output_ipa[i - 1] == u'^' and (hindi_output_ipa[i] == u'p' or hindi_output_ipa[i] == u'b')):
                hindi_output_ipa[i - 1] = "X"  
            if (hindi_output_ipa[i - 1] == u'^' and (
                    hindi_output_ipa[i] == u'\u0288' or hindi_output_ipa[i] == u'\u0256')):
                hindi_output_ipa[i - 1] = "X"
            if (hindi_output_ipa[i - 1] == u'^' and (
                    hindi_output_ipa[i] == u't\u0283' or hindi_output_ipa[i] == u'd\u0292')):
                hindi_output_ipa[i - 1] = "X"
            if (hindi_output_ipa[i - 1] == u'^' and (
                        hindi_output_ipa[i] == u'k' or hindi_output_ipa[i] == u'g' or hindi_output_ipa[
                i] == u'\u0261\u02b1\u0259')):
                hindi_output_ipa[i - 1] = "X"
            if (hindi_output_ipa[i - 1] == u'i' and hindi_output_ipa[i] == u'^'):
                hindi_output_ipa[i] = "X"
            if (hindi_output_ipa[i - 1] == u'u' and hindi_output_ipa[i] == u'^'):
                hindi_output_ipa[i] = "X"

            if (hindi_output_ipa[i - 1] == u'\u0259' and hindi_output_ipa[i] == u'-'):
                hindi_output_ipa[i - 1] = ""
                hindi_output_ipa[i] = ""
            if (hindi_output_ipa[i - 1] != u'\u0259' and hindi_output_ipa[i] == u'-'):
                hindi_output_ipa[i] = ""
            if (hindi_output_ipa[i - 1] == u'\u0259' and hindi_output_ipa[i] == u'~'):
                hindi_output_ipa[i] = "X"
            if (hindi_output_ipa[i - 1] == u'\u0259' and hindi_output_ipa[i] == u'^'):
                hindi_output_ipa[i] = "X"
            if (hindi_output_ipa[i - 1] == u'u' and hindi_output_ipa[i] == u'~'):
                hindi_output_ipa[i] = "X"
        for i in range(2, len(hindi_output_ipa)):
            if (hindi_output_ipa[i - 2] == u'i' and hindi_output_ipa[i - 1] == u':' and hindi_output_ipa[i] == u'^'):
                hindi_output_ipa[i] = ""
            if (hindi_output_ipa[i - 2] == u'u' and hindi_output_ipa[i - 1] == u':' and hindi_output_ipa[i] == u'^'):
                hindi_output_ipa[i] = "X"
            if (hindi_output_ipa[i - 2] == u'o' and hindi_output_ipa[i - 1] == u':' and hindi_output_ipa[i] == u'^'):
                hindi_output_ipa[i] = "X"
            if (hindi_output_ipa[i - 2] == u'\u1d14' and hindi_output_ipa[i - 1] == u':' and hindi_output_ipa[
                i] == u'^'):
                hindi_output_ipa[i] = "X"
            if (hindi_output_ipa[i - 2] == u'e' and hindi_output_ipa[i - 1] == u':' and hindi_output_ipa[i] == u'^'):
                hindi_output_ipa[i] = "X"
            if (hindi_output_ipa[i - 2] == u'\xe6' and hindi_output_ipa[i - 1] == u':' and hindi_output_ipa[i] == u'^'):
               
                hindi_output_ipa[i] = "X"
            if (hindi_output_ipa[i - 2] == u'a' and hindi_output_ipa[i - 1] == u':' and hindi_output_ipa[i] == u'^'):
                hindi_output_ipa[i] = "X"
            if (hindi_output_ipa[i - 2] == u'a' and hindi_output_ipa[i - 1] == u':' and hindi_output_ipa[i] == u'~'):
                hindi_output_ipa[i] = "X"
            if (hindi_output_ipa[i - 2] == u'u' and hindi_output_ipa[i - 1] == u':' and hindi_output_ipa[i] == u'~'):
                hindi_output_ipa[i] = "X"
            if (hindi_output_ipa[i - 2] == u'e' and hindi_output_ipa[i - 1] == u':' and hindi_output_ipa[i] == u'~'):
                hindi_output_ipa[i] = "X"
            if (hindi_output_ipa[i - 2] == u'o' and hindi_output_ipa[i - 1] == u':' and hindi_output_ipa[i] == u'~'):
                hindi_output_ipa[i] = "X"
            if (hindi_output_ipa[i - 1] == u'\u0259' and hindi_output_ipa[i] == u'\u1d14'):
                hindi_output_ipa[i - 1] = ""

            if (hindi_output_ipa[len(hindi_output_ipa) - 1] == "i"):
                hindi_output_ipa[len(hindi_output_ipa) - 1] = "i:"

            if (hindi_output_ipa[len(hindi_output_ipa) - 1] == "u"):
                hindi_output_ipa[len(hindi_output_ipa) - 1] = "u:"

        hindi_output = ''.join(hindi_output_ipa)

        entries['IPA Equivalent'].delete(0, END)
        entries['IPA Equivalent'].insert(0, hindi_output)
        countvo = 0
        countco = 0
        for char in hindi_output:
            if char in uvwl:
                uvwl[char] += 1
                countvo += 1
            if not char in uvwl:
                countco += 1
        if (hindi_output[-1] == u'\u0259' and countvo > 1):
            hindi_output = hindi_output[:-1]
            hindi_output = hindi_output + " "

        if (hindi_output[-1] == "i"):
            hindi_output = hindi_output + ":"
            entries['Underlying Phonemic Form'].delete(0, END)
            entries['Underlying Phonemic Form'].insert(0, hindi_output)
            

        else:
            entries['Underlying Phonemic Form'].delete(0, END)
            entries['Underlying Phonemic Form'].insert(0, hindi_output)
            


