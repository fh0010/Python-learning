#使用者輸入一段文字，程式統計字數。

sentence = [input("Word counting\nType anything : ")]

ccount = 0
wcount = 0
lcount = 0

for line in sentence:
    words = line.split()
    lcount += 1
    wcount += len(words)
    ccount += len(line)


print ("Line : %i \nWords : %i\nCharacters : %i" % (lcount, wcount, ccount))