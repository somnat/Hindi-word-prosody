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
from Syllabification import Syllabify
from IPAEquv import IPAEquivalent
from Syll_label import Labeling
from filehandling import load_file
from phoneme import Phoneme
reload(sys)
sys.setdefaultencoding('utf-8')
fields = ('Hindi Input', 'IPA Equivalent', 'Underlying Phonemic Form', 'I-Level Syllabification', 'Prosodic Label(PLSB)',
'Phoneme Level(IPA)', 'Phoneme Level(ASCII)')

def makeform(root, fields):
            entries = {}
            for field in fields:
                row = Frame(root)
                lab = Label(row, width=22, text=field + ": ", anchor='w')
                ent = Entry(row)
                ent.insert(0, "")
                row.pack(side=TOP, fill=X, padx=5, pady=5)
                lab.pack(side=LEFT)
                ent.pack(side=RIGHT, expand=YES, fill=X)
                entries[field] = ent
            return entries


if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Convert IPA Equ',
                command=(lambda e=ents: IPAEquivalent(e)))

    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='fileinputoutput',
                command=(lambda e=ents: load_file(e)))
    b2.pack(side=LEFT, padx=5, pady=5)

    b4 = Button(root, text='Syllable@Underlying Word',
                command=(lambda e=ents: Syllabify(e)))
    b4.pack(side=LEFT, padx=5, pady=5)
    b5 = Button(root, text='Label@Underlying Word',
                command=(lambda e=ents: Labeling(e)))
    b5.pack(side=LEFT, padx=5, pady=5)

    b7 = Button(root, text='Phoneme Level',
                command=(lambda e=ents: Phoneme(e)))
    b7.pack(side=LEFT, padx=5, pady=5)

    b3 = Button(root, text='Quit', command=root.quit)
    b3.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()

############################ file input output module #########################################
