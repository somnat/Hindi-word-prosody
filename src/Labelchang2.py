def Labelchanger2(hindi_output):
    hindi_output = hindi_output.replace("I", "i:")
    hindi_output = hindi_output.replace("A", "a:")
    hindi_output = hindi_output.replace("E", "e:")
    hindi_output = hindi_output.replace("O", "o:")
    hindi_output = hindi_output.replace("U", "u:")
    hindi_output = hindi_output.replace("M", u'\u0254:')
    hindi_output = hindi_output.replace("J", u'\xe6:')
    hindi_output = hindi_output.replace("N", u'\u1d14:')
    hindi_output = hindi_output.replace("P", u'p\u02b0')  # for Pha
    hindi_output = hindi_output.replace("B", u'b\u02b1')  # for bha
    hindi_output = hindi_output.replace("T", u't\u02b0')  # For ta
    hindi_output = hindi_output.replace("D", u'd\u02b1')  # for dha
    hindi_output = hindi_output.replace("Q", u'\u0288\u02b0')  # for retroflex t
    hindi_output = hindi_output.replace("c", u't\u0283')  # for ch(affiricate)
    hindi_output = hindi_output.replace("C", u't\u0283\u02b0')  # for chha
    hindi_output = hindi_output.replace("Z", u'd\u0292\u02b1')  # for jha
    hindi_output = hindi_output.replace("5", u'd\u0292')  # for ja
    hindi_output = hindi_output.replace("K", u'k\u02b0')  # for Kha
    hindi_output = hindi_output.replace("R", u'\u027d\u02b1')  # for Rha
    hindi_output = hindi_output.replace("G", u'\u0261\u02b1')
    hindi_output = hindi_output.replace("!", u'i\u0303')
    hindi_output = hindi_output.replace("#", u'i\u0303:')
    hindi_output = hindi_output.replace("%", u'u\u0303')
    hindi_output = hindi_output.replace("(", u'u\u0303:')
    hindi_output = hindi_output.replace(")", u'\u1d14\u0303:')
    hindi_output = hindi_output.replace("_", u'e\u0303:')
    hindi_output = hindi_output.replace("+", u'\xe6\u0303:')
    hindi_output = hindi_output.replace("=", u'a\u0303:')
    hindi_output = hindi_output.replace("7", u'o\u0303:')
    hindi_output = hindi_output.replace(u'`', u'\u0259\u0303')
    return hindi_output
