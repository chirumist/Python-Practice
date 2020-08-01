"""
star pattern test start
"""
f = open("../text-files/looptest.txt", "r+")
n = int(input("Star height row: \n"))
raverse = int(input("for reverse star enter 1 = 'Yes' 0 = 'No'"))
# print(raverse)
if raverse:
    for i in range(n, 0, - 1):
        for j in range(1, i + 1):
            f.write("*")
        f.write("\n")
else:
    for i in range(n, 0, 1):
        for j in range(i):
            f.write("*")
        f.write("\n")

file = f.read()

print(file)

f.close()
"""
star pattern test end
"""