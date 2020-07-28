import random

swg = {"0": 'Snack', "1": 'Water', "2": 'Gun'}
computer = random.choice(tuple(swg))

for index, gameObj in swg.items():
    print(f"Press {index} For {gameObj}")
player = 1


def gameStart():
    global player
    player = input()


def checkWin(pl, bot):
    if swg[pl] == 'Snack' and swg[bot] == 'Gun':
        print("Computer is win")
    elif swg[pl] == 'Water' and swg[bot] == 'Gun':
        print("You are win")
    elif swg[pl] == 'Gun' and swg[bot] == 'Snack':
        print("You are win")
    elif swg[pl] == 'Gun' and swg[bot] == 'Water':
        print("Computer is win")
    elif swg[pl] == 'Water' and swg[bot] == 'Snack':
        print("You are win")
    elif swg[pl] == 'Snack' and swg[bot] == 'Water':
        print("Computer is win")


game = bool(1)
while game:
    gameStart()
    if player == computer:
        print("Draw")
    else:
        checkWin(player, computer)

print(player, computer)
