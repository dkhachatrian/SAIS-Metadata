from collections import namedtuple  #immutable once stated, should be fine for the fields that never change from chapter to chapter
import fnmatch  #allow to search for strings with "wildcard" characters


###############################################
######### A bunch of declarations...###########
###############################################

DELIMITER = '\t'	#will be tab-separated CSV.


file mf = open("Metadata Fields.txt", r+)

excelHeader = ""

for line in mf:
	excelHeader = excelHeader + line + DELIMITER
#excelHeader has extra \t at end
excelHeader = excelHeader[0:-1] #cut off last \t
#excelHeader does NOT have a \n at the end

mf.close() #done with getting metadata fields from file



wordsOfInterest = {} #each word of interest will be associated via a dictionary to which field the word provides information for
#wordsOfInterest.update(["foo", "bar"], 42) would create two keys, foo and bar, which both point to 42
fieldDict = {"object" : objectType, "material" : materialType, "documentation" : docType, "creator" : creatorName} #will include the above variables as 



#########################################################
######### Some Classes and Helper Functions...###########
#########################################################

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

    def display(self):  #for debugging purposes. While printing to file, will compare metadata field term with dictionary keys before printing (makes Creator class work better)
      print(info.values()) #keys not important for metadata list

'''
class Creator(Person):
  "Person with creator role information (if known)."
    def __init__(self, name = "", email = "", institution = "", role = ""): #considering we only have informaion on the names of the authors, others default to ""
        Person.__init__(self) #calls base class
        self.info["creatorRole"] = role #adds roles to dictionary
'''
#may not actually need, can just add to dictionary manually since I know when I'm dealing with a creator Person


def findPeople(s):
	"Takes in a string known to contain names. Returns a list of Persons, to be added to Person dictionary with corresponding chapter number"
	
	people = []

	for word in s:
		if word[0].isupper() and ',' in word or if word is "and": #if it's part of a name, the first letter is capitalized
			if word has ',': #if word has comma
				name += word[:-1] #add everything except comma
			#otherwise, if word is "and", name already has entire name of Person
			person = Person(name) #make the Person
			people.append(person) #add him to list of editors
			name = "" #reset temporary name storage
		else:
			name += word #add parts of names otherwise

	return people





###################################################
######### Gaining General Information......########
###################################################

#############
########## From Table of Contents #################
#############


file toc = open("Table of Contents.txt", r+)
#Table of Contents is organized as follows:
#Book title denoted by preceding "Title: "
#Chapter titles denoted by "Chapter X: foobar" where X is a positive integer
#Authors are located two lines below chapter title. There may be two authors for a chapter.

bookTitle = ""
chapterTitles = []
editors = [] #TODO: Move "Person" class here so can use its member functions in findPerson function
authors = {} #dictionary will have the chapter number as the key and the various authors as their values

for line in toc:
	#find the book title...
	if bookTitle is "":
		x = line.rfind("Title: ") #rfind returns highest index of the substring, that is to say, in this case, right after the ' '

		if x != -1: 
			bookTitle = line[x:]	#everything after the denoter
			continue

	#find the editors...
	if editors  == [] and ", editors" in line:
		x = find(", editors")
		s = line[0:x]	#just the two names in s
		names = findPeople(s)
		editors = names	#editors not associated with any particular chapter, so can just be a list




	#get the chapter names and associate with proper numbers...
	#chapter name will be placed in the [chapter number - 1] index...
	if line.rfind("Chapter ") != -1:
		x = line.rfind("Chapter ")
		i = line.int(x) #Chapter number
		s = ""

		#pass after the chapter number
		for word in line:
			if line.index(word) < i:
				continue
			else:
				s = line[index(word):] #gets rest of line. According to requested formatting, this is the chapter name

		chapterTitles.insert(i-1, s) #inserts the chapter title in the (chapterNumber-1)th position in the list

	#will find author line by finding the "...." line preceding it
	#find the authors
	if "..." in line:
		toc.readline() #go to next line, which has just author names
		#########################################CHECK TO SEE WHETHER THE LINE ABOVE MESSES WITH THE FOR LOOP
		tempAuthors = findPeople(line)
		#current chapter (i.e., chapter to which the authors belong to) is the current length of the chapterTitles list
		#since we already added the chapter title above

		authors.update(len(chapterTitles), authors) #adds a key, chapterNumber, that has the authors (who are Persons) as their values

toc.close()
#done with table of contents

##############
######### From Files Containing Controlled Vocabulary #########
##############

#entries will be separated by a newline character ('\n')
file t = open("materials_taxonomy.csv", r+) #contains words for material types. Does not contain which words are associated with them.
#E.g., in the association "vessel" --> "ceramic", only the controlled material type "ceramic" is written on its own line.

objectTypeList = []

for line in t:
  objectTypeList.append(line)

#TODO: create "association" file that shows which words map to what. Will then change objectTypeList to a dictionary, with the appropriate keys and values. For use when parsing caption.


t.close()


###############################################
########### Main classes for Data...###########
###############################################


#TODO: may want to create a "dataLine" object to hold all these strings and have a print function for it specifically?

class DataLine:
  "Takes in a line from the captions list as a string. Parses string for information relevant for metadata input."
  #will hold data in a dictionary
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

    #above information will hopefully be read by table of contents parsing. Meaning I wouldn't need to explicitly state them here.
    publisher = "Cotsen Institute of Archaeology Press"
    pubLoc = "Los Angeles, CA"
    doi = ""
    isbn = ""


    #TODO: see if we can make arbitrary numbers of object types/material types
    cString = captionString
    figNum = getFigNum(cString)
    caption = getCaption(cString)
    copyright = "" #no figures have copyright yet
    objectTypes = [] #will compare caption text with lists that correspond to a specific object type. There may be more than one object type; when printing these will be separated via a semicolon (;)
    materialTypes = [] #similarly determined to objectType
    docType = [] #similarly determined to above two
    creatorNames = findCreators(cString) #if there is one
    creatorRoles = getCreatorRoles(creatorNames)

    #useful for definition functions
    chapterNumber = int(figNum[0])

  def getfigNum(self, s):
  	"Receives caption string. Return figure number, in the form of a string."
    x = 0
    while s[x] is not ' ':  #figure number is everything from beginning of line to first ' '
      x++
    return s[0:x] #slice from position 0 up to, but not including position x

  def getCaption(self, s):
  	"Receives entire caption string. Returns the caption (i.e., the entire string except for the figure number)."
    x = 0
    while s[x] is not ' ':
      x++
    return s[x+1:] #slice from after ' ' to end, which is entire caption

  def findCreators(self, s):
  	"Receives the entire caption string. Returns a list containing any available creator names. If known, update how "
  	#most of the time, if there is a drawing, the creator is said afterward with the introductory clause "by". Figures from outside the group of authors tend to be "courtesy of" the figure donor.

    creatorKeyPhrases = ["by", "courtesy of"] #move to declaration section?

    while len(creatorNames) is 0:
	   	for word in s:
        #will attempt to recognize keyphrases using 
        for entry in creatorKeyPhrases:
          if s[index(word):].startswith(entry):
            tempNames = ""
            for w in s[s.index(word)]: #for rest of words starting from word after by
              if i >= 10:  #determines how many other words will be in string passed to findPersons function (10 should be enough). Otherwise stops early when it reaches end of string
                break
              tempStr += w
              i++

            tempNames = findPeople(tempStr) #function checks if next word is capitalized --> whether word after by is a name


            if len(tempNames) != 0: #if it succeeded in finding names after the "by", probably the creator(s)
              creatorNames = tempNames
              #should break out of loop and function should finish by this point, because len(creatorNames) != 0

    #found creator by this point. Time to figure out his role.
    for Person in creatorNames:
      Person["creatorRole"] = ""  #give it a field in the dictionary, regardless of whether it is known. For printing to CSV

   	  if docType == "drawing" or docType == "photograph":
        Person["creatorRole"] = "Image creator" #controlled vocabulary word

  def getCreatorRoles(self, l):
    "Given a list of creators, return a list of each creator's role in the order in which the creators were located in the list."
    roles = []
    for Creator in l:
      l.append(Creator["creatorRole"])
    return roles









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


cl.close()
o.close()
