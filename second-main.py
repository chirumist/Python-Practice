"""
star pattern test start
"""
f = open("looptest.txt", "r+")
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

"""
File io example
"""
# f = open("test.txt", "r+")
# print(f.read())
# file = f.write(" thank you \n")
# print(f.read())
# f.close()
"""
Guess number count start
"""

# guesses = 8
# numbers = [2, 4, 5, 6, 9]
# guessCount = int(0)

# print(numbers)
# while guessCount <= guesses:
#     number = int(input("Guess number: \n"))
#
#     if number in numbers:
#         numbers.remove(number)
#         print("Remain number guess ", len(numbers))
#         print("remain guesses count ", guesses - guessCount)
#         if len(numbers) == 0:
#             print("All number guess with ", guessCount)
#             break
#     else:
#         print("Wrong Number guess count remain ", guesses - guessCount)
#         if guessCount == guesses - 1:
#             print("sorry your guess has been over")
#             break
#
#     guessCount = guessCount + 1


"""
Guess number count end
"""
