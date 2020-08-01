def updateSentence(assistentName, userName):
    return f"Hi, i m your assistent {assistentName}. What can i help you {userName}."


def addSum(num1,num2):
    return num1+num2


print("run program file", __name__)
if __name__ == "__main__":
    print(updateSentence("jarvis", "chirag"))
    print(addSum(10, 20))