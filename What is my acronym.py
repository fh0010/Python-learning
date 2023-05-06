#使用者輸入一段話，程式抓出單字的第一個字母，並輸出縮寫。
word = input("Enter anything : ")
a = " "

word = word.upper()
line = word.split()

for char in line:
    a = a + char[0]
print(a)


