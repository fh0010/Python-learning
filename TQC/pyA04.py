# 請撰寫一程式，讓使用者輸入兩個相同長度的字串與一個正整數 n，字串長度皆不超過128個字元，依ASCII碼表上的順序比對兩字串前n個字元，
# 最後輸出兩字串前 n 個字元的比較結果。若使用者輸入正整數 n 超過字串長度，則輸出「error」。

def compare_strings():
    str1 = input("請輸入第一個字串：")
    str2 = input("請輸入第二個字串：")
    n = int(input("請輸入正整數 n :"))

    if n > len(str1) or n > len(str2):
        print("error")
        return

    result = ""
    for i in range(n):
        if ord(str1[i]) < ord(str2[i]):
            result = "<"
        elif ord(str1[i]) > ord(str2[i]):
            result = ">"
        else:
            result = "="

    print(f"比較結果：{str1} {result} {str2}")

compare_strings()

