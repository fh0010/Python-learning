#請使用者輸入單字，判斷它是否為回文，也就是該單字前後對稱，
#例如 madam，從前讀到後或是從後讀到前的順序都是 madam。
a = input("Palindrome checker \nEnter anything : ")
ra = a.lower()
if a == (ra[::-1]):
    print("\nIs a palindrome .")
else:
    print("\nNot a palindrome !")    
