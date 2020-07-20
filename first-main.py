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

"""
User Get Value Input Dictionary Start
"""

# dic1 = {"traver": "", "franklin": "", "miracle": ""}

# print(dic1.keys(), "\nWho knows you batter")
#
# value = input("Enter player name")
# dic1[value] =input("Put " + value + " Information")
#
# print(dic1.keys())
# value = input("Enter player name")
# dic1[value] =input("Put " + value + " Information")
#
# print(dic1.keys())
# value = input("Enter player name")
# dic1[value] =input("Put " + value + " Information")
#
# print(dic1)

"""
User Get Value Input Dictionary End
"""

"""
User Get Key Value Input Dictionary Start
"""

# def update_dic():
#     f1k = input("Please Enter Your Name:")
#     f2k = input("Please Enter Your Detail:")
#     dic[f1k] = f2k


# dic = {}

# update_dic()
# update_dic()
# update_dic()

# count: int = 0

# while count <= 4:
#     update_dic()
#     count = count+1

# print(dic)


"""
User Get Key Value Input Dictionary End
"""

# My First Program
# print("Hello World")
