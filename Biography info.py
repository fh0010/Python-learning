#請使用者輸入個資，程式檢查資料是否有效，並將輸入的資訊統整，完整呈現給使用者。
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
