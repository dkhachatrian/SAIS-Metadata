from collections import namedtuple	#immutable once stated, should be fine for the fields that never change from chapter to chapter

file cl = open("SAIS Figure Caption List.txt", r) #cl = captionList. Read-only
file o = open("SAIS Metadata.csv", w+) #creates the .csv file to which we will be writing

end = cl.seek(0,2) #know ehere the end of the file is
cl.seek(0,0)	#but we should start back from the beginning

while cl.tell() is not end:	#until we reach the end of the file
	str = "" #every time, str will contain one caption
	while '\n' not in str:
		str += cl.read(1)
