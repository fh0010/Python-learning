print("Email slicer \n")

provider = {"gmail":"Google", "hotmail":"Microsoft", "yahoo":"Yahoo", "outlook":"Microsoft"}

email = input("Please enter your email : ").strip()

user = email[:email.index("@")]

