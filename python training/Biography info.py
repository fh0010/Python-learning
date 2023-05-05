while True:
    name = input("Enter your name : ")  
    if "*" in name:
        print("Do not enter * ")
        continue
    else:
        break

day = input("Enter your birthday : ")
adr = input("Enter your address : ")
gol = input("Enter your goals : ")

print("Name : "+name)
print("Birthday : "+day)
print("Address : "+adr)
print("Goal : "+gol)
