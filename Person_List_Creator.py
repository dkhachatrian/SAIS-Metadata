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



def findPeople(s, r = ""):
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

        #print(words)

        while i + p + 1 < len(words): #going through the list
                p = 0
                tempName = ""
##                print("p = " + str(p))
##                print("i = " + str(i))
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

                i = i + p + 1 #move the index down the list to be after the consecutive words (or even if they're not consecutive)

                
                
                ###NOTE: AS IT STANDS, will spit out site names and other consecutive capitalized strings of words as "names."
                ## Will be handing off generated list to Deidre, who will use it to make the list of site names.
                ## She will hand this back to me. Then I can check against these lists to ignore them instead of creating
                ## a Person out of them.


        return pList


##with open("SAIS Captions.txt", 'r', encoding = 'utf8') as f:
##        line = f.readline()
##        print(line)



with open("SAIS Captions.txt", 'r', encoding = 'utf8') as f:
        with open("Person_List.txt" , 'w') as w:
                lines = f.readlines()

                for line in lines:
                        personList = findPeople(line)

                        nameList = []

                        for person in personList:
                                name = person.fullName()
                                nameList.append(name)
        
                        if len(line.split()) > 0:
                                w.write("List of \'Persons\" found in " + line.split()[0] + " are the following: " + '\n')
                                w.write(str(nameList) + '\n')
        
