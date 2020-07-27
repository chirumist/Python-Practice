import datetime


# health-management


def getDate():
    return datetime.datetime.now()


try:
    users = {"0": "Harry", "1": "Rohan", "2": "Hammad", "3": "Chirag"}
    lock = int(input("What you want lock or retrive by press 0 for retrive or 1 for lock. \n"))
    tasks = {"0": 'diet', "1": 'excercies'}

    print("Select number for user")
    for index, user in users.items():
        print(user, index)

    selectedUser = input("Select user by enter number. \n")
    print(f"You are selected {users[selectedUser].lower()}.")

    selectedTask = input("Select diet for press 0 or excercies for 1. \n")
    print(f"You are selected {tasks[selectedTask]} .")

    if lock:
        print(f"Enter for {tasks[selectedTask]} \n")
        stopWriting = 1
        text = ""
        while stopWriting:
            text += "\n"
            text += str(getDate())
            text += ' - ' + input()
            stopWriting = int(input("press 0 for exit and press 1 for continue "))
            print(f"You are select {stopWriting}")
            if stopWriting == 1:
                print("Please Continue")
            else:
                break

        with open('../text-files/health-management/' + users[selectedUser].lower() + '-' + tasks[selectedTask] + '.txt', 'a') as fp:
            fp.write(text)
            pass
    else:
        print("Process for retrive for diet or excercies \n")
        with open('../text-files/health-management/' + users[selectedUser].lower() + '-' + tasks[selectedTask] + '.txt', 'r') as fp:
            print(fp.read())
            pass
except Exception as e:
    print(e)
