
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

        def displayName(self):
                print(self.info["firstName"] + ' ' + self.info["lastName"])

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


#result = findPeople("William H. Isbell", "creator")
#                    01234567891111111
#                              0123456

##result = findPeople("""
##2.17	One of the four personages depicted on the Gateway of the Kalasasaya blowing a trumpet
##and holding a severed human head. Redrawn by Stanislava Chávez
##from Posnansky (1945, Vol. I:Plate XXXIX.3).""", "editor")

##result = findPeople("""2.18	a) Examples from the Gatewayof the Kalasasaya showing the conch shell
##associated with other appendages, in one case bird and in the other “fish,” in the crowns of profile personages.
##Redrawn by Stanislava Chávez from Posnansky (1945, Vol. I:Plate XLIII.2-3), b) One of two winged personages on
##a Provincial Pucara textile carrying what appears to be a
##conch shell. Drawn by Stanislava Chávez from a color photograph of the textile provided by William Isbell.""", "creator")
##
##for person in result:
##        person.displayName()        



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


##for person in editors:
##        person.display()
##
##
##print(authors)
##
##print('\n')
##
##for i in range(1,27):
##        x = str(i)
##        aList = authors[x]
##
##        print("These are the authors found for Chapter "+ x + ": ")
##
##        for person in aList:
##                person.display()
##
##        print('\n')
##
##
##print(chapterTitles)
