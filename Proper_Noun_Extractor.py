

def findProperNouns(s, r = ""):
        "Takes in a string known to contain names. Returns a list of Persons, to be added to Person dictionary with corresponding chapter number"

        words = s.split() #split the string at spaces
        n = len(words)
        x = 0

        while x < n: #for each word in the list
                if not (words[x])[0].isupper():#if the word is not capitalized
                        words.remove(words[x])#remove it from the list
                        x -= 1 #check the new word in the x'th position
                        n -= 1 #update length of array
#                elif ',' in words[x]:#if word has comma attached to it (and hasn't been removed from the list already)
#                        words[x] = words[x][:-1]#slice it out (ought to be at the end of the word)
#                elif '.' in words[x] and len(words[x]) > 2: #if word has period and longer than two chars, it's not a middle initial, it's at the end of a sentence. Slice out '.'
#                        words[x] = words[x][:-1]
                x += 1

        tempPhrase = ""
        p = 0
        i = 0
        wList = []

        #print(words)

        while i + p + 1 < len(words): #going through the list
                p = 0
                tempPhrase = ""
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


                
#                if p > 0: #if there are more than zero words after the word of interest that come consecutively
                for x in range(p): #concatenate them (up to p
                        tempPhrase = tempPhrase + words[i+x] + ' '
                tempPhrase += words[i+p] #for p, do not add space at the end
                        

                if tempPhrase != "":
                        #person = Person(tempName, r) #make the person
                        wList.append(tempPhrase) #add person to list

                i = i + p + 1 #move the index down the list to be after the consecutive words (or even if they're not consecutive)

                
                
                ###NOTE: AS IT STANDS, will spit out site names and other consecutive capitalized strings of words as "names."
                ## Will be handing off generated list to Deidre, who will use it to make the list of site names.
                ## She will hand this back to me. Then I can check against these lists to ignore them instead of creating
                ## a Person out of them.


        return wList


##with open("SAIS Captions.txt", 'r', encoding = 'utf8') as f:
##        line = f.readline()
##        print(line)



with open("SAIS Captions.txt", 'r', encoding = 'utf-8-sig') as f:
        with open("Capitalized_Word_List.txt" , 'wb') as w:
                lines = f.readlines()

                for line in lines:
                        #personList = findPeople(line)
                        wordList = findProperNouns(line)
                        #nameList = []

                        #for person in personList:
                        #        name = person.fullName()
                        #        nameList.append(name)
        
                        if len(line.split()) > 0:
                                w.write(bytes("List of capitalized phrases found in " + line.split()[0] + " are the following: " + '\n', 'utf8'))
                                for word in wordList:
                                        w.write(bytes(word + '\t', 'utf8'))
                                for x in range(2):
                                        w.write(bytes('\n', 'utf8')) #twice to make it easier on the eyes to separate captions
        
