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
##		x = 0
##		while name[x] != ' ':
##			x -= 1
##		x += 1 #go back to after ' '
##		return name[x:]#returns slice from after last ' ' to end, i.e., last name

	def getFirstName(self, name): #first name is first word in name
                return name.split()[0]
#		return (name[:name.find(self.getLastName(name))])[0:-1] #slices out the last space after the first name but before the LastName

	def display(self):  #for debugging purposes. While printing to file, will compare metadata field term with dictionary keys before printing (makes Creator class work better)
		#print(info.values()) #keys not important for metadata list
		print(self.info)

### TEST CASES ###
#
#dude = Person("John Doe", "author")
#
#dude.display()



def findPeople(s, r):
        "Takes in a string known to contain names. Returns a list of Persons, to be added to Person dictionary with corresponding chapter number"

        words = s.split() #split the string at spaces
        n = len(words)

        for x in range(n): #for each word in the list
                if !(words[x][0].isupper()):#if the word is not capitalized
                        words.remove(word)#remove it from the list
                        x -= 1 #check the new word in the x'th position
                        n -= 1 #update length of array
                elif ',' in words[x]:#if word has comma attached to it (and hasn't been removed from the list already)
                        words[x] = words[x][:-1]#slice it out (ought to be at the end of the word)
                elif '.' in words[x] and words[x] > 2: #if word has period and longer than two chars, it's not a middle initial, it's at the end of a sentence. Slice out '.'
                        words[x] = words[x][:-1]

        tempName = ""
        p = 0
        i = 0
        pList = []

        while i + p + 1 < len(words): #going through the list
                p = 0
                
                while s.find(words[i+p]) + len(words[i+p]) == s.find(words[i+p+1]): #while the next capitalized word in the list is directly after the word we're looking at right now
                        p += 1 #check the next name; keep track of how many are consecutive

                if p > 0: #if there are more than zero words after the word of interest that come consecutively
                        for x in range(p + 1): #concatenate them (up to and including the value p (hence p+1)
                                tempName += words[i+x]

                if tempName != "":
                        person = Person(tempName, r)
                        pList.append(person)
                        
                
                ###NOTE: AS IT STANDS, will spit out site names and other consecutive capitalized strings of words as "names."
                ## Will be handing off generated list to Deidre, who will use it to make the list of site names.
                ## She will hand this back to me. Then I can check against these lists to ignore them instead of creating
                ## a Person out of them.


        return pList

##        tempName = ""
##        p = -1
##
##        for i in range(n - 1):#for the n'th word in the list
##        
##                if s.find(words[i]) + len(words[i]) == s.find(words[i+1]): #if the (n+1)'th word is directly after the n'th word in the string
##                        if len(words[i+1]) == 2 and words[i+1][1] == '.': #if the n+1'th word is two chars long and ends in '.' (i.e., is a middle initial)
##                                if i + 2 < n and s.find(words[i+1]) + len(words[i+1]) == s.find(words[i+2]): #if the n+2'th word is directly after the n+1'th word
##                                        p = 2 #store entries n and n+1 and n+2 as a single name
##                        else: #else if there's a period, means at the end of a sentence, not important, slice out
##                                #if the role r is "editor" or "author"
##                                        #store entries n and n+1 as a single name
##                                #if the role is "creator"
##                                        #if the entries from the list personKeyPhrases comes before entry n
##                                                #store entries n and n+1 as a single name

        #for each name that was taken
                #put Person(name, r) in a list people

        #return people

        







##
##        #working with the lines from the table of contents (i.e., only the names and possibly commas and "and"'s
##
##        people = []
##        wordsComma = s.split(',')
##        wordsAnd = s.split(" and ")
##        names = []
##
##        for word in wordsAnd:
##                names.extend(word.split(','))
##
##        n = 0
##        for word in names:
##                if word == "":
##                        n += 1
##
##        for x in range(0,n):
##                names.remove("")
##
##        for name in names:
##                person = Person(name, r) #Error! Need person's role!
##                people.append(person)
##                        
##        return people
##
##






##        people = []
##        name = ""
##        words = s.split()       #splits at ' '
##        wordsCap = []
##
##        for word in words:
##                if word[0].isupper():
##                        if '.' in word and len(word) > 2:
##                                wordsCap.append(word[:-1])      #if not a middle initial, remove period
##                        else:
##                                wordsCap.append(word)
##                
##
##
##        
##        wordsComma = s.split(',')
##        wordsAnd = s.split(" and ")
##        
##
##        print(wordsComma)
##        
##
##


                 
##
##        for word in s:
##                if (word[0].isupper() and ',' in word) or word is "and": #if it's part of a name, the first letter is capitalized
##                        if ',' in word: #if word has comma
##                                name += word[:-1] #add everything except comma
##                        #otherwise, if word is "and", name already has entire name of Person
##                        person = Person(name, r) #make the Person
##                        people.append(person) #add him to list of editors
##                        name = "" #reset temporary name storage
##                else:
##                        name += word #add parts of names otherwise

##        return people


result = findPeople("William H. Isbell", "creator")

for person in result:
        person.display()        




##
##
##
###############
############ From Table of Contents #################
###############
##
##
##toc = open("Table of Contents.txt", 'r')
##
##tocLines = toc.readlines()
##
###Table of Contents is organized as follows:
###Book title denoted by preceding "Title: "
###Chapter titles denoted by "Chapter X: foobar" where X is a positive integer
###Authors are located two lines below chapter title. There may be two authors for a chapter.
##
##dotsFound = False #will be used to find the authors
##
##bookTitle = ""
##chapterTitles = []
##editors = [] #TODO: Move "Person" class here so can use its member functions in findPerson function
##authors = {} #dictionary will have the chapter number as the key and the various authors as their values
##
##for line in tocLines:
##        #find the book title...
##        if bookTitle is "":
##                x = line.find("Title: ")
##
##                if x != -1: 
##                        x += len("Title: ")     #puts x after "Title: "
##                        bookTitle = line[x:]    #everything after the denoter
##                        continue
##
##        #find the editors...
##        if editors  == [] and ", editors" in line:
##                x = line.find(", editors")
##                s = line[0:x]   #just the two names in s
##                names = findPeople(s, "editor")
##                editors = names #editors not associated with any particular chapter, so can just be a list
##
##
##
##
##        #get the chapter names and associate with proper numbers...
##        #chapter name will be placed in the [chapter number - 1] index...
##        if "Chapter " in line:
##                x = line.find("Chapter ")
##                x += len("Chapter ") #puts x right after "Chapter "
##
##                
##                tempNum = -1
##                if line[x:x+2].isdigit():
##                        tempNum = line[x:x+2]   #if chapter number is in double digits
##                elif line[x].isdigit(): #chapter number in single digits
##                        tempNum = line[x]
##                        
##                if tempNum != -1:
##                        i = int(tempNum) #Chapter number
##                else:   #bad!
##                        pass
##
##                
##                s = ""
##
##                
##                #pass after the chapter number
##                for word in line:
##                        if line.index(word) < i:
##                                continue
##                        else:
##                                s = line[line.index(word):] #gets rest of line. According to requested formatting, this is the chapter name
##
##                chapterTitles.insert(i-1, s) #inserts the chapter title in the (chapterNumber-1)th position in the list
##
##        #will find author line by finding the "...." line preceding it
##        #find the authors
##        if "..." in line:
##                dotsFound = True
##                continue #go to next line, which has just author names
##                #########################################CHECK TO SEE WHETHER THE LINE ABOVE MESSES WITH THE FOR LOOP
##        if dotsFound:
##                dotsFound = False
##                tempAuthors = findPeople(line, "author")
##
##                print(tempAuthors)
##                break
##                #current chapter (i.e., chapter to which the authors belong to) is the current length of the chapterTitles list
##                #since we already added the chapter title above
##
##                authors[str(len(chapterTitles))] = tempAuthors #adds a key, chapterNumber, that has the authors (who are Persons) as their values
##
###print(bookTitle)
##print(authors)
###print(editors)
###print(chapterTitles)
##
##toc.close()
###done with table of contents
##
