from collections import namedtuple	#immutable once stated, should be fine for the fields that never change from chapter to chapter

file cl = open("SAIS Figure Caption List.txt", r) #cl = captionList. Read-only
file o = open("SAIS Metadata.csv", w+) #creates the .csv file to which we will be writing

end = cl.seek(0,2) #know ehere the end of the file is
cl.seek(0,0)	#but we should start back from the beginning

while cl.tell() is not end:	#until we reach the end of the file
	str = "" #every time, str will contain one caption
	while '\n' not in str:
		str += cl.read(1)
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







###########
########### 		Dealing With Printing To File/Caption Logic
###########



file cl = open("SAIS Figure Caption List.txt", r) #cl = captionList. Read-only
file o = open("SAIS Metadata.csv", w+) #creates the .csv file to which we will be writing


end = cl.seek(0,2) #know ehere the end of the file is
cl.seek(0,0)	#but we should start back from the beginning

while cl.tell() is not end:	#until we reach the end of the file
	str = "" #every time, str will contain one caption
	while '\n' not in str:
		str += cl.read(1) #add one byte at a time (1 byte = 1 char)

string printS #what will be printed to file


figNum = ""
caption = ""

strLoc = 0

while str[strLoc] is not '.':	#gets past chapter number
	strLoc++

strLoc++	#gets past '.' after chapter number

while str[strLoc] is not ' ':	#fig number from after '.' to ' '
	figNum += str[strLoc]

caption = str[strLoc:]	#caption is everything after the first ' '













