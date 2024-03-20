import random

bored = [' _ |', ' _ |', ' _ |',
         ' _ |', ' _ |', ' _ |',
         ' _ |', ' _ |', ' _ |']
# x = 'X'
# o = 'O'
player = ''
robot = ''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_over = False
def Bored():
    print('___+____+____+__')
    print(bored[0],bored[1],bored[2])
    print('___+____+____+__')
    print(bored[3], bored[4], bored[5])
    print('___+____+____+__')
    print(bored[6], bored[7], bored[8])
    print('___+____+____+__')
def Game_over():
    global game_over
    if (bored[0] == bored[1] == bored[2] != ' _ |') or \
        (bored[3] == bored[4] == bored[5] != ' _ |') or \
        (bored[6] == bored[7] == bored[8] != ' _ |') or \
        (bored[0] == bored[3] == bored[6] != ' _ |') or \
        (bored[1] == bored[4] == bored[7] != ' _ |') or \
        (bored[2] == bored[5] == bored[8] != ' _ |') or \
        (bored[0] == bored[4] == bored[8] != ' _ |') or \
        (bored[2] == bored[4] == bored[6] != ' _ |'):
        game_over = False
        return "Win"
    elif ' _ |' not in bored:
        game_over = False
        return "tie"
    else:
        return "play"

selected_choice = True

def Choice():
    global player, robot
    while selected_choice:
        choose = input("You want to play with X or O ?").upper()
        if choose == 'X':
            player = 'X'
            robot = 'O'
            return choose
        elif choose == 'O':
            player = 'O'
            robot = 'X'
            return choose
        else:
            print("Invalid char, Please choose X or O.")
            Choice()
            return

def player_move():
    # while True:
        try:
            p1 = int(input("Choose your move! 1-9 "))
            while p1 not in numbers:
                p1 = int(input("Please choose between 1 to 9"))
                if bored[p1-1] != ' _ |':
                    p1 = int(input("Position is taken, please choose another one: "))
            bored[p1 - 1] = " " + player + " |"
            numbers.remove(p1)
            print('player ', numbers)
            # robot_move = random.choice(numbers)
            # bored[robot_move - 1] = " " + robot + " |"
            # numbers.remove(robot_move - 1)
            # print(numbers)
            # Bored()
            # break
        except ValueError:
            print("Sorry, that was not a valid integer. Please try again.")

def Robot_move():
    try:
        robot_move = random.choice(numbers)
        while robot_move not in numbers:
            robot_move = random.choice(numbers)
        bored[robot_move - 1] = " " + robot + " |"
        numbers.remove(robot_move)
        print('robo ', numbers)
        Bored()
    except ValueError:
        print("Sorry, that was not a valid integer. Please try again.")


def Game():
    global game_over
    Choice()
    Bored()
    while not game_over:
        result = Game_over()
        player_move()
        result = Game_over()
        if result == 'Win':
            Bored()
            print("You Won!")
            game_over = True
            break
        Robot_move()
        result = Game_over()
        if result == 'Win':
            Bored()
            print("Ops! you lost ;)")
            game_over = True
            break

Game()