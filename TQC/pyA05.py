#  請撰寫一程式，讓使用者輸入一個 1~9 位數的數字，輸出每一個數字相乘的算式及結果

def multiply_digits():
    num = input("請輸入一個 1~9 位數的數字：")

    if not num.isdigit() or len(num) < 1 or len(num) > 9:
        print("輸入無效！請確保輸入為 1~9 位數的數字。")
        return

    result = 1
    equation = ""
    for digit in num:
        digit_int = int(digit)
        result *= digit_int
        equation += str(digit_int) + " * "
    equation = equation.rstrip(" * ")  # 移除最後一個多餘的 "*"
    equation += f" = {result}"
    print(equation)

multiply_digits()


