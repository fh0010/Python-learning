# 請撰寫一程式，包含名為 compute()的函式，接收主程式傳遞的一個期中考分數，
# compute()判斷分數值，若分數在 0~100 以外，則回傳「-1」；若分數大於等於 60，則加 5 分；否則一律加 10 分，回傳至主程式輸出。

def compute():
    
    if a > 100 or a< 0:
        print("-1")
    elif a > 60:
        a += 5
    else:
        a += 10    


a = int(input("Enter any number "))

compute(a)