"""
Falty calculator start
"""


def cal(operator, firstnum, secondnum):
    if operator == "+":
        res = firstnum + secondnum
        if firstnum == 56 and secondnum == 9 or firstnum == 9 and secondnum == 56:
            print(77)
        else:
            print(res)
        startCal()

    elif operator == "-":
        res = firstnum + secondnum
        print(res)
        startCal()

    elif operator == "*":
        res = firstnum * secondnum
        if firstnum == 45 and secondnum == 3 or firstnum == 3 and secondnum == 45:
            print(555)
        else:
            print(res)
        startCal()

    elif operator == "/":
        res = firstnum * secondnum
        if firstnum == 56 and secondnum == 6 or firstnum == 6 and secondnum == 56:
            print(4)
        else:
            print(res)
        startCal()
    else:
        print("Invalid operator please try again")
        startCal()


def startCal():
    print("Enter operators ", ["+", "-", "*", "/"])
    operator = input("Enter operator")
    firstnum = int(input("Enter first number"))
    secondnum = int(input("Enter second number"))
    if operator == "exit":
        print("Exit this program")
    else:
        cal(operator, firstnum, secondnum)


startCal()


"""
Falty calculator end
"""
