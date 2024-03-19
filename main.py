import random

bored = [' _ |', ' _ |', ' _ |',
         ' _ |', ' _ |', ' _ |',
         ' _ |', ' _ |', ' _ |']
# x = 'X'
# o = 'O'
player = ''
robot = ''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def Bored():
    print('___+____+____+__')
    print(bored[0],bored[1],bored[2])
    print('___+____+____+__')
    print(bored[3], bored[4], bored[5])
    print('___+____+____+__')
    print(bored[6], bored[7], bored[8])
    print('___+____+____+__')

selected_choice = True

def Choice():
    while selected_choice:
        choose = input("You want to play with X or O ?").upper()
        if choose == 'X':
            player = 'X'
            robot = 'O'
            return
        elif choose == 'O':
            player = 'O'
            robot = 'X'
            return
        else:
            print("Invaild char, Please choose X or O.")
            Choice()
            return

def player_move():
    while True:
        try:
            p1 = int(input("Choose your move! 1-9 "))
            break
        except ValueError:
            print("Sorry, that was not a valid integer. Please try again.")
        except not in numbers:
            print("Please, choose number between 1 to 9")


def Game():
    Choice()
    Bored()
    player_move()
Game()