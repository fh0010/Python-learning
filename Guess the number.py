#請使用者猜一個介於範圍（例如 1 到 50）之間的數字，若使用者猜錯，就詢問他們想繼續玩還是退出；
#若使用者猜對，就顯示祝賀訊息，並統計使用者的嘗試次數。如果使用者輸入的數字超出設定範圍，就顯示錯誤提示。
import random

num = random.randrange(1,50)
count = 1
try:
    gus = int(input("Guess a number between 1 to 50 : "))
    while gus != num :
        if gus > num :
            print("Guess lower than "+str(gus))
            gus = int(input("Guess a number between 1 to 50 : "))
            count += 1
        else:
            print("Guess higher than "+str(gus))
            gus = int(input("Guess a number between 1 to 50 : "))
            count += 1

    print("You guessed the number correctly ! \n")
    print("You tried "+str(count)+" times !!! ")

except ValueError:
    print("Please enter number !!!")

