global countv
global countc 
uvwl = {u'\u0259': 0, u'u': 0, u'E': 0, u'M': 0, u'A': 0, u'O': 0, "J": 0, "N": 0, u'i': 0, u'a': 0,
        u'U': 0, u'I': 0, u'!': 0, u'#': 0, u'%': 0, u'(': 0, u')': 0, u'_': 0, u'+': 0, u'=': 0, u'1': 0, u'`': 0}
def countvowel(hindi_output):
    countc=0
    countv=0
    for char in hindi_output:
	  if char in uvwl:
	      uvwl[char]+=1
	      countv +=1
	  if not char in uvwl:
	      countc+=1
    return countv,countc
