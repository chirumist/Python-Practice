"""
Guess number count start
"""

guesses = 8
numbers = [2, 4, 5, 6, 9]
guessCount = int(0)

print(numbers)
while guessCount <= guesses:
    number = int(input("Guess number: \n"))

    if number in numbers:
        numbers.remove(number)
        print("Remain number guess ", len(numbers))
        print("remain guesses count ", guesses - guessCount)
        if len(numbers) == 0:
            print("All number guess with ", guessCount)
            break
    else:
        print("Wrong Number guess count remain ", guesses - guessCount)
        if guessCount == guesses - 1:
            print("sorry your guess has been over")
            break

    guessCount = guessCount + 1


"""
Guess number count end
"""
