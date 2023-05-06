#計算帳單的小費。可以請使用者輸入帳單金額，然後顯示一定比例的小費。別忘了要四捨五入。
#更進階的話，可以請使用者輸入分配人數，然後算出小費總額與分擔平均。
#再進一步，還可以不平均分配，例如 1 個人承擔 70% 的帳，30% 則由剩下的人承擔，算出每個人必須承擔的金額。

print ("Tip calculator")
while True:
    try:
        num = int(input("How much is the bill today ? \nEnter : "))
        tip = int(input("What  persentage will you tip ? \nEnter : "))
        per = int(input("How many people ? \nEnter : "))
        break

    except ValueError:
        print("Please enter number !!!")
        continue

ctip = "%.2f"%(tip/100*num)
tol = "%.2f"%(num+(tip/100*num))
div = "%.2f"%((num+(tip/100*num))/per)

print ("Under the condition of "+str(tip)+" % tip , the tip will be "+ctip+" , totall will be "+tol)
print ("Divided with "+str(per)+" person , each person will be "+div)