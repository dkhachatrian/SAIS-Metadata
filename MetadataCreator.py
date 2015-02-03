from collections import namedtuple	#immutable once stated, should be fine for the fields that never change from chapter to chapter
import fnmatch	#allow to search for strings with "wildcard" characters


#########
#########	A bunch of declarations...
#########

#universal metadata terms

bookTitle = "Images in Action: The South Andean Iconographic Series"
yearOfPub = ""
bookDesc - ""
editorName1 = "William H. Isbell"
editorName2 = "Mauricio	Uribe"
publisher = "Cotsen Institute of Archaeology Press"
pubLoc = "Los Angeles, CA"
doi = ""
isbn = ""

#when printing, separate with comma (,)

excelHeader = "Book title,Year,Description,Editor first name,Editor last name,Editor first name,Editor last name,Publisher,Publisher location,DOI,ISBN,Chapter,Chapter title,Author first name,Author last name,Email,Affiliated institution,Figure number,Caption,Copyright,Object type,Material type,Documentation type,Creator first name,Creator last name,Creator first name,Creator last name,Creator role,Cultural term,Site name,Date type,Start date,End date,Temporal terms,Latitude max,Latitude min,Longitude max,Longitude min,Projection,Geographic keywords"
#^will print at the top of each chapter's metadata spreadsheet

#same within each chapter
#make (albeit large) lists, where the cell number corresponds to the chapter number
#list[i] -> Chapter (i+1)

#if all the information of an author is known, group together as one Author "struct"

class Author():
    def __init__(self, name, email, institution):
        self.m_name = name
        self.m_email = email
        self.m_inst = institution


#chapterNumber can be determined by the index number
chapterTitles = ["",
"Identification, Definition, and Continuities of the Yaya-Mama Religious Tradition in the Titicaca Basin",
"Late Formative Period Ceramics from Pukara: Insights from Excavations on the Central Pampa",
"Stone Stelae of the Southern Basin: A Stylistic Chronology of Ancestral Personages", 
]
authorOnePerChapter =
authorTwoPerChapter = 
#TODO: fill in rest of the chapter titles



#We can also potentially have the script only deal with caption logic,
#as the fields that are the same within each chapter are relatively simple and quick to do by hand







###########
########### 		Dealing With Printing To File/Caption Logic
###########


#TODO:
#Make dictionary of words of interest and the words they map to (if not themselves)
#Have a master wordsOfInterest to which we will compare each word in the caption
#If the word matches to a term in the dictionary


#Example Code
#myDict = {}
#myDict.update(dict.fromkeys(['a', 'b', 'c'], 10))
#myDict.update(dict.fromkeys(['b', 'e'], 20))
#
#
#gives a dictionary of the form
#{'a': 10, 'b': 20, 'c': 10, 'd': 10, 'e': 20}

#So I can see making the lists/arrays of words as their own separate things (in case we change the word we wish to map them to),
#concatenating them to make our big dictionary,
#checking to see if we find a word of interest in our caption, and
#if so, placing our field appropriately.


#TODO: may want to create a "dataLine" object to hold all these strings and have a print function for it specifically?




wordsOfInterest = {} #each word of interest will be associated via a dictionary to which field the word provides information for

figNum = ""
caption = ""
copyright = "" #no figures have copyright yet
objectType = "" #will compare caption text with lists that correspond to a specific object type
materialType = "" #similarly determined to objectType
docType = "" #similarly determined to above two
creatorName = "" #if there is one

fieldDict = {"object" : objectType, "material" : materialType, "documentation" : docType, "creator" : creatorName} #will include the above variables as 

file cl = open("SAIS Figure Caption List.txt", r) #cl = captionList. Read-only
file o = open("SAIS Metadata.csv", w+) #creates the .csv file to which we will be writing



end = cl.seek(0,2) #know ehere the end of the file is
cl.seek(0,0)	#but we should start back from the beginning

while cl.tell() is not end:	#until we reach the end of the file (rest of code should occur here)
	str = "" #every time, str will contain one caption
	while '\n' not in str:
		str += cl.read(1) #add one byte at a time (1 byte = 1 char)

	string printS #what will be printed to file




	strLoc = 0

	while str[strLoc] is not '.':	#gets past chapter number
		strLoc++

	strLoc++	#gets past '.' after chapter number

	while str[strLoc] is not ' ':	#fig number from after '.' to ' '
		figNum += str[strLoc]

	caption = str[strLoc:]	#caption is everything after the first ' '

	for word in caption:
		if word in wordsOfInterest:
			whichField = wordsOfInterest.get(word) #have string that describes field. Use to pick which string to fill in
			fieldDict[whichField] = word 	#gives each variable the appropriate value


	#THE FOLLOWING PIECE OF CODE ASSUMES THAT NOTHING ELSE WILL NEED TO BE PRINTED AFTER DETERMINING THE FIELDS LOCATED IN THE DICTIONARY fieldDict
	#THIS MAY NOT ACTUALLY BE THE CASE

	for x in xrange[0: len(fieldDict)]:	#for every in the dictionary
		o.write("\""+fieldDict.values()[x]+"\"")	#print out the field value with quotes around it, so that internal punctuation does not mess up the reading of the resulting .csv file
													#(CHECK TO SEE IF FIELDS OF DICT ARE IN CORRECT ORDER)

		if x is not len(fieldDict):
			o.write(",")	#to denote the next field
		else:
			o.write('\n')	#otherwise, go to next line  <-- pay attention to this, may need to change!











