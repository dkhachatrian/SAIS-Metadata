#from collections import namedtuple  #immutable once stated, should be fine for the fields that never change from chapter to chapter
#import fnmatch  #allow to search for strings with "wildcard" characters
#from collections import queue #may want to change my lists to queues? (Since using FIFO for printing)

#Turns out I haven't needed to import anything yet...

###############################################
######### A bunch of declarations...###########
###############################################

DELIMITER = '\t'  #will be tab-separated CSV.
PERSONS_MAX = 3 #total number of people of a specific type, e.g. Creator or Author, in a row. Determined by Metadata Fields.txt. To simplify code, all the different types of people have the same max.


mf = open("Metadata Fields.txt", 'r')

excelHeader = ""
metadataFields = []

for line in mf:
	metadataFields.append(line[:-1])    #line[:-1] removes '\n' from line
	excelHeader = excelHeader + line[:-1] + DELIMITER
#excelHeader has extra \t at end
excelHeader = excelHeader[0:-1] #cut off last \t
#excelHeader does NOT have a \n at the end

mf.close() #done with getting metadata fields from file

### DEBUGGING ###
#print(metadataFields)
#print(excelHeader)


wordsOfInterest = {} #each word of interest will be associated via a dictionary to which field the word provides information for
#wordsOfInterest.update(["foo", "bar"], 42) would create two keys, foo and bar, which both point to 42
fieldDict = {"object" : objectType, "material" : materialType, "documentation" : docType, "creator" : creatorName} #will include the above variables as 



#########################################################
######### Some Classes and Helper Functions...###########
#########################################################

#person to be used to determine first and last name
class Person():
        "A Person has a name, a role in the book (e.g. author, editor, creator), and possibly an email and/or institution."

        def __init__(self, name = "", title = "", email = "", institution = ""): #considering we only have informaion on the names of the authors, others default to ""
                self.info = {}

                self.info["firstName"] = self.getFirstName(name)
                self.info["lastName"] = self.getLastName(name)
                self.info["title"] = title #title says whether the Person is an author, creator, editor, etc.
                self.info["email"] = email
                self.info["institution"] = institution
                #self.name = name
                #self.email = email
                #self.inst = institution

        def getLastName(self, name):  #last name is rest of name
                n = len(name.split()[0]) + len(' ') #everything that we need to skip to get last name
                return name[n:]
                
                ###Commented out code would have middle initials in the first name, only last word in last name
##              x = 0
##              while name[x] != ' ':
##                      x -= 1
##              x += 1 #go back to after ' '
##              return name[x:]#returns slice from after last ' ' to end, i.e., last name

        def getFirstName(self, name): #first name is first word in name
                return name.split()[0]
#               return (name[:name.find(self.getLastName(name))])[0:-1] #slices out the last space after the first name but before the LastName

        def display(self):  #for debugging purposes. While printing to file, will compare metadata field term with dictionary keys before printing (makes Creator class work better)
                #print(info.values()) #keys not important for metadata list
                print(self.info)

        def fullName(self):
                return self.info["firstName"] + ' ' + self.info["lastName"]

### TEST CASES ###

##dude = Person("John H. Doe", "author")
##
##dude.display()


def findPeople(s, r):
        "Takes in a string known to contain names. Returns a list of Persons, to be added to Person dictionary with corresponding chapter number"

        words = s.split() #split the string at spaces
        n = len(words)
        x = 0

        while x < n: #for each word in the list
                if not (words[x])[0].isupper():#if the word is not capitalized
                        words.remove(words[x])#remove it from the list
                        x -= 1 #check the new word in the x'th position
                        n -= 1 #update length of array
                elif ',' in words[x]:#if word has comma attached to it (and hasn't been removed from the list already)
                        words[x] = words[x][:-1]#slice it out (ought to be at the end of the word)
                elif '.' in words[x] and len(words[x]) > 2: #if word has period and longer than two chars, it's not a middle initial, it's at the end of a sentence. Slice out '.'
                        words[x] = words[x][:-1]
                x += 1

        tempName = ""
        p = 0
        i = 0
        pList = []

##        print(words)

        while i + p + 1 < len(words): #going through the list
                
                tempName = ""
##                print("Are words consecutive? " + str((s.find(words[i+p]) + len(words[i+p]) + len(' ') == s.find(words[i+p+1]))))
##                print("First word checked is "+ str(words[i+p]))
##                print("Index of first word checked is " + str(s.find(words[i+p])))
##                print("Length of first word checked is " + str(len(words[i+p])))
##                print("Possible consecutive word is " + str(words[i+p+1]))
##                print("Index of possible consecutive word is " + str(s.find(words[i+p+1])))                
##                
                while (i+p+1 < len(words)) and (s.find(words[i+p]) + len(words[i+p]) + len (' ') == s.find(words[i+p+1])): #while the next capitalized word in the list is directly after the word we're looking at right now
                        p += 1 #check the next name; keep track of how many are consecutive


                
                if p > 0: #if there are more than zero words after the word of interest that come consecutively
                        for x in range(p): #concatenate them (up to p
                                tempName = tempName + words[i+x] + ' '
                        tempName += words[i+p] #for p, do not add space at the end
                        

                if tempName != "":
                        person = Person(tempName, r) #make the person
                        pList.append(person) #add person to list

##                print("p at the end of a cycle of the loop, before reinitialization, is " + str(p))
                
                i = i + p + 1 #move the index down the list to be after the consecutive words (or even if they're not consecutive)
                p = 0

##                print("p at the end of a cycle of the loop, after reinitialization, is " + str(p))
##                print("i at the end of a cycle of the loop is " + str(i))                
##                
                ###NOTE: AS IT STANDS, will spit out site names and other consecutive capitalized strings of words as "names."
                ## Will be handing off generated list to Deidre, who will use it to make the list of site names.
                ## She will hand this back to me. Then I can check against these lists to ignore them instead of creating
                ## a Person out of them.


        return pList



def getNum(s):
        '''
Takes in a string. Returns the first integer found in the string, as an int.
        '''
        nString = ""
#        print("s in getNum is " + s)
        
        for x in range(len(s)):
                if s[x].isdigit():
                        nString = nString + s[x]
##                        print("x = " + str(x))
##                        print(" s]x] = " + s[x])
##                        print("nString = " + nString)
                        continue

                if nString != "":
                        break

        return int(nString)
                

        


def getWordInQuotes(s):
    "Takes in a string. Returns a string with the contents of the first word or phrase enveloped in double-quotes."
    "Returns an empty string if no quotes in string."
    "(For use with files containing lists of interest.)"
    "For example, \"I like pie!\" will return the string literal 'I like pie!' (with no '' surrounding it)."

    contents = ""
    i = j = 0

    if '\"' in s:
        i = s.find('\"')
        i += 1 #goes to right after the first quote

    if '\"' in s[i:]: #if another quote in rest of string, get it
        j = s.rfind('\"')
        if j == -1: #prevent backslicing if not located
            j = 0

    if i >= 0 and j > 0:
        contents = s[i:j]

#    print(i)
#    print(j)
#    print(contents)

    return contents

test = "="
#print(getWordInQuotes(test))

##### TEST CASES ###
##
##extraQuotes = "\"I like pie!\""
##withoutQuotes = getWordInQuotes(extraQuotes)
##noQuotes = "I like pie!"
##
##print(withoutQuotes)
##print(extraQuotes)
##print(noQuotes)


def listToString(l, d):
	"Given a list l, returns a string with the values of the list separated by the delimiter passed in, d."
	"(Will not have delimiter at the end of the string.)"
	"If passed in a list of Persons, the function will call getPertinentPersonInfo and use its result in creating the string it returns."
	s = ""

	for entry in l:
		if entry is str:
			s = s + entry + d
		elif entry is Person: #does this work? if not, fix!
			s = s + getPertinentPersonInfo(entry) + d

	s = s[:-1] #cuts off last delimiter

	return s


def writeCSVHeaderToFile(l, f):
	"Given a list of metadata headers in the proper order, writes them to file in the order given, separated by the appropriate delimiter."
	"Inserts newline at the end of printing all the headers."

	for entry in l:
		f.write(entry + DELIMITER)

	f.seek(-1, 1)
	f.write('\n')

def getPertinentPersonInfo(d):
	"Given a dictionary containing a Person's data, return a string necessary for writing to CSV (first and last name, role if a creator)."
	"Will not have delimiter at end of string."
	"(ORDER OF FIELDS IS HARDWIRED INTO CODE. Need to change if order of metadata fields changes.)"

	s = ""

	s = d["firstName"] + DELIMITER + d["lastName"]

	if d["title"] == "creator":
		s += DELIMITER + d["creatorRole"]

	return s
	
def getMatchesFromString(s, d):
	"Given a string, returns a list of the values for keys recognized in the string, in the order in which they appear in the string."
	l = []

	for key in d:
		if key in s:
			l.append(d[key])

	return l

def numberOfInstancesOf(x, s):
	"Given a string s, returns the number of times x appears in s."
	n = 0

	for x in s:
		n += 1

	return n

###################################################
######### Gaining General Information......########
###################################################

#############
########## From Table of Contents #################
#############


#NOTE: CURRENTLY NEEDS DOTS IN LINE PRECEDING NAMES TO FIND AUTHORS
# CURRENTLY ONLY OBTAINS FIRST PERSON

with open("Table of Contents.txt", 'r', encoding = 'utf8') as toc:
        tocLines = toc.readlines()

        #Table of Contents is organized as follows:
        #Book title denoted by preceding "Title: "
        #Chapter titles denoted by "Chapter X: foobar" where X is a positive integer
        #Authors are located two lines below chapter title. There may be two authors for a chapter.

        dotsFound = False #will be used to find the authors

        bookTitle = ""
        chapterTitles = []
        editors = [] #TODO: Move "Person" class here so can use its member functions in findPerson function
        authors = {} #dictionary will have the chapter number as the key and the various authors as their values

        for line in tocLines:
                #find the book title...
                if bookTitle is "":
                        x = line.find("Title: ")

                        if x != -1: 
                                x += len("Title: ")	#puts x after "Title: "
                                bookTitle = line[x:]	#everything after the denoter
                                continue

                #find the editors...
                if editors  == [] and ", editors" in line:
                        x = line.find(", editors")
                        s = line[0:x]	#just the two names in s
                        names = findPeople(s, "editor")

##                        for person in names:
##                                person.display()
                                
                        editors = list(names)	#editors not associated with any particular chapter, so can just be a list




                #get the chapter names and associate with proper numbers...
                #chapter name will be placed in the [chapter number - 1] index...
                if "Chapter " in line:
                        x = line.find("Chapter ")
                        x += len("Chapter ") #puts x right after "Chapter "
                        i = getNum(line[x:]) #Chapter number
                        x += len(str(i)) + len(": ") #put x right at the beginning of the chapter name
                        y = len(line) - 1 #minus one to remove the newline character if there are no dots

                        if '...' in line:
                                y = line.index("..")
                                
                        
                        s = line[x:y] #slice from after the chapter number to before the dots, if there are any)
                                       

#                        print("s = " + s)                                                              
                        chapterTitles.insert(i-1, s) #inserts the chapter title in the (chapterNumber-1)th position in the list

                #will find author line by finding the "...." line preceding it
                #find the authors
                if "..." in line:
                        dotsFound = True
                        continue #go to next line, which has just author names
                        #########################################CHECK TO SEE WHETHER THE LINE ABOVE MESSES WITH THE FOR LOOP
                if dotsFound:
                        dotsFound = False
                        tempAuthors = findPeople(line, "author")
                        #current chapter (i.e., chapter to which the authors belong to) is the current length of the chapterTitles list
                        #since we already added the chapter title above

##                        print("For Chapter " + str(len(chapterTitles)) + ": ")
##                        for person in tempAuthors:
##                                
##                                person.display()

                        

                        authors[str(len(chapterTitles))] = list(tempAuthors) #adds a key, chapterNumber, that has the authors (who are Persons) as their values
                        #copy.deepcopy is not needed because the Persons in the list shouldn't be deleted

#done with table of contents


#NOTE: needs three dots the line before the names to find properly


##############
######### From Files Containing Controlled Vocabulary #########
##############

#text files are structured so that the master list of all possible entries starts with a "{". All entries are enclosed in quotes ("").
#Associations are denoted in the following way: the entry from the master list is written first, followed by an equals sign "=",
#followed by words that map to this first word, also in quotes.
#Each newline corresponds to a new masterword being mapped.

otl = open("objectType_list.txt", 'r') #object type list
mtl = open("materialType_list.txt", 'r') #material type list
dtl = open("docType_list.txt", 'r') #document type list

objectTypeDict = {}
materialTypeDict = {}
docTypeDict = {}


def formDictionaryfromFile(d, f):
    "Takes in a file with lines indicating dictionary values and associated keys. Forms the corresponding dictioary from this file."
    "The values of the dictionary are lists."
    "(Specifics as to file format is given in comments above.)"

    lines = f.readlines()
    word = ""

    for line in lines:
        word = ""
        
        words = line.split()
#        print(words)
        
        x = 0
        n = len(words)
            
        while x < n:
#            print(x)
            s = getWordInQuotes(words[x])
            if s == "":     #if returns empty string, no "" in word, not one of the desired words
                words.remove(words[x])
                n = len(words) #to update the length of list, equivalent to " n -= 1 "
            else:
                words[x] = s #otherwise update with non-quoted word
                x += 1

        #print(words)

        
        if '{' in line and len(d) == 0: #'{' is what's used to recognize it's the line with all the keys
            for entry in words:
                d.setdefault(entry,[]).append(entry) #if the caption has the specific word itself, it maps to itself (i.e., a stela is a stela...)
                #setdefault checks to see if entry is in d (it shouldn't be); if not, it makes d[entry] = []. The append function then adds entry to the newly formed list

        #above if statement should occur before anything else. Use this to check which word to

        

        elif '=' in line and len(words) > 0 and words[0] in d.keys():   #'=' is used to recognize it has the words associated to the keys
            for x in range(1,len(words)):
                d.setdefault(words[0],[]).append(words[x])
        



formDictionaryfromFile(objectTypeDict, otl)
formDictionaryfromFile(materialTypeDict, mtl)
formDictionaryfromFile(docTypeDict, dtl)

print(objectTypeDict)
print(materialTypeDict)
print(docTypeDict)

#should have dictionaries I want. Don't need lists anymore.

otl.close()
mtl.close()
dtl.close()



###############################################
########### Main classes for Data...###########
###############################################


#TODO: may want to create a "dataLine" object to hold all these strings and have a print function for it specifically?

class DataLine:
	"Takes in a line from the captions list as a string upon initialization. Parses string for information relevant for metadata input and stores the data in a dictionary."
	#will hold data in a dictionary
	def __init__(self, captionString = ""):
		data = {} #will hold data in dictionary

		#keys of 'data' are chosen to match with the keys placed in metadataFields, to handle order of printing.
		#For cases where there may be multiple fields for information held in one object, e.g. the names of the editors or creators (which are held in a list),
		#the key is named after the after the first metadata field pertaining to them (e.g. "Editor 1 First Name"), and the key points to a string that can be directly written to file.

		###   UNIVERSAL METADATA TERMS  ###

		data["Book Title"] = bookTitle
		#bookTitle is variable found in "Getting information from Table of Contents" section
		data["Year"] = ""
		data["Description"] - ""



		editorsToBeWritten = getPertinentPersonInfo(editors) 
		#editors is variable found in "Getting information from Table of Contents" section

		data["Editor 1 first name"] = editorsToBeWritten

		#above information will hopefully be read by table of contents parsing. Meaning I wouldn't need to explicitly state them here.
		data["Publisher"] = "Cotsen Institute of Archaeology Press"
		data["Publisher location"] = "Los Angeles, CA"
		data["DOI"] = ""
		data["ISBN"] = ""

		###   METADATA TERMS THAT VARY BY CHAPTER  ###

		#useful for definition of functions
		chapterNumber = int(figNum[0])
		data["Chapter"] = chapterNumber
		data["Chapter Title"] = chapterTitles[chapterNumber - 1] #chapter title i is stored in the (i-1)'th position in the chapterTitles lists.
		#chaperTitles is variable found in "Getting information from Table of Contents" section


		chapterAuthors = authors[chapterNumber] #returns a list of 1 or more authors, if implemented properly.
		#authors is variable found in "Getting information from Table of Contents" section
		data["Author 1 first name"] = listToString(chapterAuthors, DELIMITER) #listToString will call "getPertinentPersonInfo" function if list is composed of Persons.


		###   METADATA TERMS THAT VARY BY FIGURE  ###

		cString = captionString

		figNum = getFigNum(cString)
		data["Figure number"] = figNum

		caption = getCaption(cString)
		data["Caption"] = caption

		copyright = "" #no figures have copyright yet
		data["Copyright"] = copyright

		objectTypes = getMatchesFromString(cString, objectTypeDict)
		data["Object type"] = listToString(objectTypes, ';')

		materialTypes = getMatchesFromString(cString, materialTypeDict) #similarly determined to objectType
		data["Material type"] = listToString(materialTypes, ';')

		docTypes = getMatchesFromString(cString, docTypeDict) #similarly determined to above two
		data["Documentation type"] = listToString(docTypes, ';')

		#Special note: the documentation type of "photograph" is assumed unless one of the other documentation types is evident from the caption text.

		creators = findCreators(cString) #if there is one
#    creatorRoles = getCreatorRoles(creatorNames) #function should be unnecessary by using getPertinentPersonInfo
		creatorsToBeWritten = getPertinentPersonInfo(creators)
		data["Creator 1 first name"] = creatorsToBeWritten


	def getfigNum(self, s):
		"Receives caption string. Return figure number, in the form of a string."
		x = 0
		while s[x] is not ' ':  #figure number is everything from beginning of line to first ' '
			x += 1
		return s[0:x] #slice from position 0 up to, but not including position x

	def getCaption(self, s):
		"Receives entire caption string. Returns the caption (i.e., the entire string except for the figure number)."
		x = 0
		while s[x] is not ' ':
			x += 1
		return s[x+1:] #slice from after ' ' to end, which is entire caption

	def findCreators(self, s):
		"Receives the entire caption string. Returns a list containing any available creator names. If known, update their role."
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
							i += 1

						tempNames = findPeople(tempStr) #function checks if next word is capitalized --> whether word after by is a name


						if len(tempNames) != 0: #if it succeeded in finding names after the "by", probably the creator(s)
							creatorNames = tempNames
							#should break out of loop and function should finish by this point, because len(creatorNames) != 0

		#found creator by this point. Time to figure out his role.
		for Person in creatorNames:
			Person["creatorRole"] = ""  #give it a field in the dictionary, regardless of whether it is known. For printing to CSV

			if docType == "drawing" or docType == "photograph":
				Person["creatorRole"] = "Image creator" #controlled vocabulary word

 # def getCreatorRoles(self, l):
 #   "Given a list of creators, return a list of each creator's role in the order in which the creators were located in the list."
 #   roles = []
 #   for Creator in l:
 #     l.append(Creator["creatorRole"])
 #   return roles


	def writeToFile(self, f):
		"Given a file, writes out its own contents to the files, according to the order in which the fields are written."
		"(Checks order by comparing keys of itself to list of metadata fields.)"

		############  NOTE: If data from a Person ends up needing to be printed in several locations on the metadata, this will have to be changed.

		s = ""
		editorsWritten = false
		authorsWritten = false
		creatorsWritten = false

		for key in metadataFields:  #follows the order of the metadata fields given! So don't need to worry about that
			if key in self.data:
				#if self.data[key] is list:
				#  s = listToString(self.data[key])
				#else:
				if "editor" in lower(key) and editorsWritten == false:
					editorsWritten = True
				if "author" in lower(key) and authorsWritten == false:
					authorsWritten = True
				if "creator" in lower(key) and creatorsWritten == false:
					creatorsWritten = True

				t = self.data[key]
			#need to make it so that string passed in for printing has correct amount of delimiters! Because this will prevent empty cells being written for editors/authors/creators.
				if ("editor" in lower(key) and editorsWritten == True) or ("author" in lower(key) and authorsWritten == True) or ("creator" in lower(key) and creatorsWritten == True):
					s = listToString(self.data[key])
					n = numberOfInstancesOf(DELIMITER, s) #implement

					#in the end, there needs to be (number of pertinent data entries for person, n1)*(number of people to be printed, n2) - 1 because f.write(s+DELIMITER) takes care of one of them.
					#Each Person has three pieces of information that do not need to be printed, as they are not provided (email, institution) or used internally (title).
					#So n1 = len(t.info) - 3
					#n2 = PERSONS_MAX
					#number of extra DELIMITERs to be printed is n1*n2-(n+1)
					n1 = len(t.info) - 3
					xd = n1 * PERSONS_MAX - (n+1)

					for x in xrange[0, xd]:
						s += DELIMITER

				else:
					s = t

			else:
				s = ""  #means we don't have that information from the caption (not in dataLine's dictionary).

				f.write(s + DELIMITER)  #after going through all of them, will have extra DELIMITER at end, need to change to newline
		
		#after printing all the appropriate values
		f.seek(-1, 1) #goes one byte, i.e. one character, to the left from the current position (which should be the current end of the file)
		f.write('\n') #prints the newline, so that file is in correct position to be written by next newline file.
									#will need to remove last newline character at the very end of the file.










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









cl = open("SAIS Figure Caption List.txt", 'r') #cl = captionList. Read-only
o = open("SAIS Metadata.csv", 'w') #creates the .csv file to which we will be writing

writeCSVHeaderToFile(metadataFields, o)

for line in cl:
	lineOfData  = DataLine(line)
	writeToFile(lineOfData, o)

o.seek(-1, 2) #goes right before very last character in file
o.truncate() (#removes final unnecessary newline character)

cl.close()
o.close()
