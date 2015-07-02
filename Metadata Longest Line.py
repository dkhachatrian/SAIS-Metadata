with open("SAIS Captions.txt", 'r', encoding = 'utf-8') as captions:

    lines = captions.readlines()

    maxNum = -1
    maxLen = -1
    maxLine = ""
    i = 0
    tempLen = -1

    for line in lines:
        i += 1
        tempLen = len(line)

        if tempLen > maxLen:
            maxNum = i
            maxLen = tempLen
            maxLine = line

    with open("SAIS Longest Caption.txt", 'w') as f:
        f.write("The longest caption is in line "+ str(maxNum) + " of \"SAIS Captions.txt\".")
        f.write('\n')
        f.write("The caption length is "+ str(maxLen) + " characters.")
        f.write('\n')
        f.write("The caption reads as the following: " + maxLine)

