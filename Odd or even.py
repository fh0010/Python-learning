#寫一個程式，當使用者輸入一個介於一定範圍（例如 1 到 1000）的數字，它能夠辨別奇偶，並輸出檢驗結果給使用者。
num = float(input("Please enter 1 ~ 1000 \n: "))

if (num%2)== 0 :
    print("Even")
else:
    print("Odd")
