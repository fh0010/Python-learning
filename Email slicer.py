#請用戶輸入 Email 地址，然後判斷它是自定義域名還是熱門域名。
print("Email slicer \n")

provider = {"gmail":"Google", "hotmail":"Microsoft", "yahoo":"Yahoo", "outlook":"Microsoft"}

email = input("Please enter your email : ")
email = ('\033[2;46;41m'+email+'\033[0;0m')

username = email.split("@")[0]
userdoma = email.split("@")[-1]
userdomain = userdoma.split(".")[0]


if userdomain in provider.keys():
    print (f"It seems {email} is registered under {provider[userdomain]} !")
else:
    print (f"({email} is registered under custom domain at {userdomain} !")    
