a = input("Palindrome checker \nEnter anything : ")
ra = a.lower()
if a == (ra[::-1]):
    print("\nIs a palindrome .")
else:
    print("\nNot a palindrome !")    
