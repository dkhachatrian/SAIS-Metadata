#Caption_Sanitizer.py

""" Will remove all tabs in SAIS Captions.txt and replace them with spaces.
	This new file will be saved as SAIS Captions Sanitized.txt	"""


with open("SAIS Captions.txt", 'r', encoding = 'utf-8-sig') as r:
	with open("SAIS Captions Sanitized.txt", 'w', encoding = 'utf-8-sig') as w:
		for line in r:
			cleanedLine = line
			if '\t' in cleanedLine:
				cleanedLine = line.replace('\t', ' ')
			print(cleanedLine)
			w.write(cleanedLine)
