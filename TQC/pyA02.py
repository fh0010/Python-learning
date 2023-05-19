# 請撰寫一程式，讓使用者輸入分數，若分數大於 60 分，則加 10 分，否則加 5 分，最後輸出調整後的分數。
# 若使用者輸入的分數在 0~100 以外，則輸出「error」。

a = int(input("Enter any number "))

if a > 100 or a < 0 :
    print("error")

elif a > 60:
    a += 10
    print(a)
else:
    a += 5
    print(a)

