word = input("Enter anything : ")
a = " "

word = word.upper()
line = word.split()

for char in line:
    a = a + char[0]
print(a)


