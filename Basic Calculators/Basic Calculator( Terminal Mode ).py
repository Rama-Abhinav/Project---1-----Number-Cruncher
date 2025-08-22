# +, -, /, *, **, 1/x, sqaure-root, percentage

def Operations():
    User_Num = int(input("enter num: "))
    User_Sign = input("Enter sign: ").strip()
    Next_Num = 0

    def Add(Num,Sign):
        if Sign == '+':
            global Next_Num
            Next_Num = int(input("Enter Next Number: "))
            Equal_to = input("Enter '=' Symbol to get result: ")
            if Equal_to == "=":
                print(f"Sum of {Num} and {Next_Num} = {Num + Next_Num}")

    def Difference(Num,Sign):
        if Sign == '-':
            global Next_Num
            Next_Num = int(input("Enter Next Number: "))
            Equal_to = input("Enter '=' Symbol to get result: ")
            if Equal_to == "=":
                print(f"Difference of {Num} and {Next_Num} = {Num - Next_Num}")

    def Multiply(Num,Sign):
        if Sign == 'x':
            global Next_Num
            Next_Num = int(input("Enter Next Number: "))
            Equal_to = input("Enter '=' Symbol to get result: ")
            if Equal_to == "=":
                print(f"Product of {Num} and {Next_Num} = {Num * Next_Num}")

    def Divide(Num,Sign):#-------------------------------------------------------------Use This Sign:  ÷
        if Sign == '÷':
            global Next_Num
            Next_Num = int(input("Enter Next Number: "))
            Equal_to = input("Enter '=' Symbol to get result: ")
            if Equal_to == "=":
                print(f"Division of {Num} and {Next_Num} = {Num / Next_Num}")

    def Percentage(Num, Sign):
        if Sign == "%":
            NumInPercent = Num/100
            Equal_to = input("Enter '=' Symbol to get result: ")
            if Equal_to == "=":
                print(f"{Num}% in decimal = {NumInPercent}")

    def Exponent(Num,Sign):
        if Sign == '^':
            global Next_Num
            Power_Num = int(input("Enter Power To Which the Number is to be Raised: "))
            Equal_to = input("Enter '=' Symbol to get result: ")
            if Equal_to == "=":
                print(f"{Num} to the power of {Power_Num} = {(Num ** Power_Num)}")

    def Root(Num,Sign):#---------------------------------------------------------------Use This Sign: √
        if Sign == '√':
            global Next_Num
            RootOfNum = int(input("Enter Root Number(2 < root < ∞): "))
            Equal_to = input("Enter '=' Symbol to get result: ")
            if Equal_to == "=":
                print(f"{RootOfNum} root of {Num} = {Num ** (1/RootOfNum)}")

    def OneByX(Num,Sign):
        if Sign == '1/x':
            Equal_to = input("Enter '=' Symbol to get result: ")
            if Equal_to == "=":
                print(f"1/{Num} = {round(1/Num, 2)}")


    while True:

        Add(User_Num, User_Sign)
        Difference(User_Num,User_Sign)
        Multiply(User_Num, User_Sign)
        Divide(User_Num, User_Sign)
        Percentage(User_Num, User_Sign)
        Exponent(User_Num, User_Sign)
        Root(User_Num, User_Sign)
        OneByX(User_Num, User_Sign)

        Ask = input("Try again(Y/N): ").upper().strip()
        if Ask == 'Y':
            User_Num = int(input("enter num: "))
            User_Sign = input("Enter sign: ")
            continue
        elif Ask == 'N':
            break

Operations()
