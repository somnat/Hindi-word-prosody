def Labelchanger1(hindi_output):
    hindi_output = hindi_output.replace("i:", "I")
    hindi_output = hindi_output.replace("a:", "A")
    hindi_output = hindi_output.replace("e:", "E")
    hindi_output = hindi_output.replace("o:", "O")
    hindi_output = hindi_output.replace("u:", "U")
    hindi_output = hindi_output.replace(u'\u0254:', "M")
    hindi_output = hindi_output.replace(u'\xe6:', "J")
    hindi_output = hindi_output.replace(u'\u1d14:', "N")
    hindi_output = hindi_output.replace(u'p\u02b0', "P")  # for Pha
    hindi_output = hindi_output.replace(u'b\u02b1', "B")  # for bha
    hindi_output = hindi_output.replace(u't\u02b0', "T")  # For ta
    hindi_output = hindi_output.replace(u'd\u02b1', "D")  # for dha
    hindi_output = hindi_output.replace(u'\u0288\u02b0', "Q")  # for retroflex t
    hindi_output = hindi_output.replace(u't\u0283', "c")  # for ch(affiricate)
    hindi_output = hindi_output.replace(u't\u0283\u02b0', "C")  # for chha
    hindi_output = hindi_output.replace(u'd\u0292\u02b1', "Z")  # for jha
    hindi_output = hindi_output.replace(u'd\u0292', "5")  # for ja
    hindi_output = hindi_output.replace(u'k\u02b0', "K")  # for Kha
    hindi_output = hindi_output.replace(u'\u027d\u02b1', "R")  # for Rha
    hindi_output = hindi_output.replace(u'\u0261\u02b1', "G")  # for gha
    hindi_output = hindi_output.replace(u'i\u0303', "!")
    hindi_output = hindi_output.replace(u'i\u0303:', "#")
    hindi_output = hindi_output.replace(u'u\u0303', "%")
    hindi_output = hindi_output.replace(u'u\u0303:', "(")
    hindi_output = hindi_output.replace(u'\u1d14\u0303:', ")")
    hindi_output = hindi_output.replace(u'e\u0303:', "_")
    hindi_output = hindi_output.replace(u'\xe6\u0303:', "+")
    hindi_output = hindi_output.replace(u'a\u0303:', "=")
    hindi_output = hindi_output.replace(u'o\u0303:', "7")
    hindi_output = hindi_output.replace(u'\u0259\u0303', u'`')

    return hindi_output

