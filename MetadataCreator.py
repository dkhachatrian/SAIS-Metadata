from collections import namedtuple  #immutable once stated, should be fine for the fields that never change from chapter to chapter
import fnmatch  #allow to search for strings with "wildcard" characters


###############################################
######### A bunch of declarations...###########
###############################################

DELIMITER = '\t'	#will be tab-separated CSV. (May want to change to tab-delimited?)




metadataFields = ["Book title","Year","Description","Editor first name","Editor last name","Editor first name","Editor last name","Publisher","Publisher location","DOI","ISBN","Chapter","Chapter title","Author first name","Author last name","Email","Affiliated institution","Figure number","Caption","Copyright","Object type","Material type","Documentation type","Creator first name","Creator last name","Creator first name","Creator last name","Creator role","Cultural term","Site name","Date type","Start date","End date","Temporal terms","Latitude max","Latitude min","Longitude max","Longitude min","Projection","Geographic keywords"]
excelHeader = ""

for entry in metadataFields:
	excelHeader = excelHeader + entry + DELIMITER
#excelHeader has extra \t at end


excelHeader = excelHeader[0:-1] #cut off last \t
#excelHeader does NOT have a \n at the end


#######################################################################
######### Gaining General Information from Table of Contents...########
#######################################################################


#TODO: automate getting the names of the chapter titles and author names
#chapterNumber can be determined by the index number
chapterTitles = ["",
"Identification, Definition, and Continuities of the Yaya-Mama Religious Tradition in the Titicaca Basin",
"Late Formative Period Ceramics from Pukara: Insights from Excavations on the Central Pampa",
"Stone Stelae of the Southern Basin: A Stylistic Chronology of Ancestral Personages", 
]
authorOnePerChapter =
authorTwoPerChapter = 
#TODO: fill in rest of the chapter titles
#same within each chapter
#make (albeit large) lists, where the cell number corresponds to the chapter number
#list[i] -> Chapter (i+1)


file toc = open("Table of Contents.txt", r+)
#Table of Contents is organized as follows:
#Book title denoted by preceding "Title: "
#Chapter titles denoted by "Chapter X: foobar" where X is a positive integer
#Authors are located two lines below chapter title. There may be two authors for a chapter.

bookTitle = ""
editors = [] #TODO: Move "Person" class here so can use its member functions in findPerson function



def findPerson(s):


for line in toc:
	if bookTitle is "":
		x = line.rfind("Title: ") #rfind returns highest index of the substring, that is to say, in this case, right after the ' '

		if x != -1: 
			bookTitle = line[x:]	#everything after the denoter
			continue

	if editors  == []:
		






wordsOfInterest = {} #each word of interest will be associated via a dictionary to which field the word provides information for

#wordsOfInterest.update(["foo", "bar"], 42) would create two keys, foo and bar, which both point to 42

fieldDict = {"object" : objectType, "material" : materialType, "documentation" : docType, "creator" : creatorName} #will include the above variables as 

###############################################
########### Main classes for Data...###########
###############################################

#person to be used to determine first and last name
class Person():
    def __init__(self, name = "", email = "", institution = ""): #considering we only have informaion on the names of the authors, others default to ""
        self.info = {}

        self.info["firstName"] = getFirstName(name)
        self.info["lastName"] = getLastName(name)
        self.info["email"] = email
        self.info["institution"] = institution
        #self.name = name
        #self.email = email
        #self.inst = institution

    def getLastName(self, name):  #last name is always last word in name
      x = 0
      while name[x] is not ' ':
        x--
      x++ #go back to after ' '
      return name[x:]#returns slice from after last ' ' to end, i.e., last name

    def getFirstName(self, name): #first name may have middle initial. Easiest to return everything except last name
      return (name - getLastName(name))[0:-1] #slices out the last space after the first name but before the LastName

    def display(self):
      print(info.values()) #keys not important for metadata list







#We can also potentially have the script only deal with caption logic,
#as the fields that are the same within each chapter are relatively simple and quick to do by hand







###########
###########     Dealing With Printing To File/Caption Logic
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


#TODO: will have file of list of terms to be put in fields of metadata. Parse file, create the lists of object types and material types.
#Map the words that appear in the captions to one of these terms (probably via dictionary)







#TODO: may want to create a "dataLine" object to hold all these strings and have a print function for it specifically?
#Will contain meat of the script
class DataLine:
  "Will hold functions that parse the caption string, and have a print function appropriate for comma-separated .csv's."
  "To be used while looping through caption list file"
  def __init__(self, captionString = ""):
    data = {} #will hold data in dictionary

    #universal metadata terms
    data["bookTitle"] = "Images in Action: The South Andean Iconographic Series"
    data["yearOfPub"] = ""
    data["bookDesc"] - ""

    editor1 = Person("William H. Isbell") #First Editor
    data["editor1FirstName"] = editor1["firstName"]
    data["editor1LastName"] = editor1["lastName"]

    editor2 = Person("Mauricio Uribe") #second editor
    data["editor2FirstName"] = editor2["firstName"]
    data["editor2LastName"] = editor2["lastName"]
    publisher = "Cotsen Institute of Archaeology Press"
    pubLoc = "Los Angeles, CA"
    doi = ""
    isbn = ""

    cString = captionString
    figNum = getFigNum(cString)
    caption = getCaption(cString)
    copyright = "" #no figures have copyright yet
    objectType = "" #will compare caption text with lists that correspond to a specific object type
    materialType = "" #similarly determined to objectType
    docType = "" #similarly determined to above two
    creatorName = findCreator(cString) #if there is one

    #useful for definition functions
    chapterNumber = int(figNum[0])

  def getfigNum(self, s):
    x = 0
    while s[x] is not ' ':  #figure number is everything from beginning of line to first ' '
      x++
    return s[0:x] #slice from position 0 up to, but not including position x

  def getCaption(self, s):
    x = 0
    while s[x] is not ' ':
      x++
    return s[x+1:] #slice from after ' ' to end, which is entire caption

   def findCreator(self, s):
   	#most of the time, if there is a drawing, the creator is said afterward with the introductory clause "by"



   	if objectType == "drawing":




file cl = open("SAIS Figure Caption List.txt", r) #cl = captionList. Read-only
file o = open("SAIS Metadata.csv", w+) #creates the .csv file to which we will be writing

'''
end = cl.seek(0,2) #know ehere the end of the file is
cl.seek(0,0)  #but we should start back from the beginning
while cl.tell() is not end: #until we reach the end of the file (rest of code should occur here)
  line = "" #every time, str will contain one caption
  while '\n' not in str:
    str += cl.read(1) #add one byte at a time (1 byte = 1 char)
  string printS #what will be printed to file
'''

for line in cl:
  lineOfData  = DataLine(line)

'''
  strLoc = 0
  while str[strLoc] is not '.': #gets past chapter number
    strLoc++
  strLoc++  #gets past '.' after chapter number
  while str[strLoc] is not ' ': #fig number from after '.' to ' '
    figNum += str[strLoc]
  caption = str[strLoc:]  #caption is everything after the first ' '
  for word in caption:
    if word in wordsOfInterest:
      whichField = wordsOfInterest.get(word) #have string that describes field. Use to pick which string to fill in
      fieldDict[whichField] = word  #gives each variable the appropriate value
  #THE FOLLOWING PIECE OF CODE ASSUMES THAT NOTHING ELSE WILL NEED TO BE PRINTED AFTER DETERMINING THE FIELDS LOCATED IN THE DICTIONARY fieldDict
  #THIS MAY NOT ACTUALLY BE THE CASE
  for x in xrange[0: len(fieldDict)]: #for every in the dictionary
    o.write("\""+fieldDict.values()[x]+"\"")  #print out the field value with quotes around it, so that internal punctuation does not mess up the reading of the resulting .csv file
                          #(NEED TO CHECK TO SEE IF FIELDS OF DICT ARE IN CORRECT ORDER)
    if x is not len(fieldDict):
      o.write(",")  #to denote the next field
    else:
      o.write('\n') #otherwise, go to next line  <-- pay attention to this, may need to change!
'''



