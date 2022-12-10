"""Morse code translator
    Translates things to morse according to the file "morse-code.txt"
    which has the values for each symbol in a comma separated manner
    special characters not supported: #%\ ºª ñç¨{}[]¨
"""
with open('D:\MEGA\Python\Proyectos-varios-python\morse-translator\morse-code.txt') as f:
    morsecode = f.readlines()

morsedict = {}
humandict = {}
for code in morsecode:
    code = code.strip("\n")
    try:
        key,morse = code.split(",")
    except ValueError:
        key,morse = (",","--..--")
    morsedict[key] = morse
    humandict[morse] = key

def tomorsetranslator(text: str):
    translation = ""
    wordlist = text.upper().split(" ")
    for j,word in enumerate(wordlist):
        for i,letter in enumerate(word):
            if i == len(word)-1 and j == len(wordlist)-1:
                translation += morsedict[letter]
            elif i == len(word)-1:
                translation += morsedict[letter] + "    "
            else:
                translation += morsedict[letter] + " "
                
    return translation

def tohumantranslator(htext:str):
    htranslation = ""
    hwordlist = htext.split(r"    ")
    for hword in hwordlist:
        hword = hword.split(" ")
        for hi,hletter in enumerate(hword):
            if hi == len(hword)-1:
                htranslation += humandict[hletter] + " "
            else:
                htranslation += humandict[hletter]
    return htranslation

#Testing if everything works correctly
tomorse = tomorsetranslator("a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 . , ? ' ! / ( ) & : ; = + - _ \" $ @")
tohuman = tohumantranslator(tomorse)

print(tohuman,tomorse, sep= "\n")
