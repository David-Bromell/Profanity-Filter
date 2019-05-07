import nltk, re, pprint
import PyPDF2, pythonwin
from nltk import word_tokenize

#Taking user input
DFile = input('Enter Database File Name/Path: ')
CFile = input('Enter Content File Name/Path: ')

#Importing the database and content
D = open(DFile)
C = open(CFile)

#Reading the files and storing them in another variable
Dr = D.read()
Cr = C.read()

#Tokenizing the raw data and storing them in their respective variables
Dt = word_tokenize(Dr)
Ct = word_tokenize(Cr)

#Displaying the original text and it's tokenized version
print ('\n')
print ('This is the original text: ')
print (Cr)
print ('\n')
print ('This is the original text tokenized: ')
print (Ct)

#Getting the length of the two tokenized texts
Dl = len(Dt)
Cl = len(Ct)

#Counter Declaration & Initialization
count1 = 0
count2 = 0

#THE FILTER

for count1 in range(0,Cl):
    for count2 in range(0,Dl):
        if Ct[count1] == Dt[count2]:
            Ct[count1] = '*****'
 
#The New Text
print ('\n')
print ('The Filtered Text Is: ')
print (Ct)

#Output Text as File
#Cdt = detokenize(Ct)
#OP = open("Filtered.txt","w")
#OP.write(Ct)

