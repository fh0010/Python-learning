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