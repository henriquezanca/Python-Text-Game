import random

# Life Points
lifepoints = 100

# Places
def leftside():
    print('\nYou see a brown bear... What you do?')
    print('Attack or Run?')

    answer = input(':').lower()

    if answer == 'attack':
        attack = random.randint(100, 100)
        new_lpoints = lifepoints - attack
        print(f'Are you crazy?')
        gameover('You Died')
    elif answer == 'run':
        print('You run for your life and drop on a hole')
        print('\n')
        hole()
    else:
        gameover("Jesus, just choose an action!")

def rightside():
    print('You see a road and a house on the end... What you do? ')
    print('Walking or Enter')

    answer = input(':').lower()

    if answer == 'enter':
        print("You see a house full of money bags on the floor, let's catch it! ")
        print('Catch or Leave')
        
        catch_or_leave = input(':').lower()

        if catch_or_leave == 'catch':
            print('YEAH BOY! You are rich now!')
            win()
        elif catch_or_leave == 'leave':
            gameover('Are you insane? You lost it')
        else:
            gameover('Hard choice?')
    
    elif answer == 'walking':
        gameover("Well... You keep walking, hope you find your path. Bye!")
    else:
        gameover('Jesus you really dont know how to choose')


def hole():
    print('You see yourself in a dark hole... But you see a door? What? Two doors? One Red and one Blue ')
    print('Red or Blue?')

    answer = input(':').lower()

    if answer == 'red':
        print('You are teleported to a road... ')
        print('\n')
        rightside()
    elif answer == 'blue':
        bluedoor()
    else:
        print("You don't know how to choose? ")
        print('\n')
        gameover()    

def bluedoor():
    win()

# Win
def win():
    print('You Win! Thanks for playing =)')
    play_again()


# Game Over 
def gameover(reason):
    print('\n' + reason)
    print('Game Over!')
    play_again()

# Play Again
def play_again():
    print('\nDo you want to play again? (y/n)')

    answer = input(':').lower()

    if 'y' in answer:
        startgame()
    else:
        exit() 

# Start Game 
def startgame():
    print('----- Welcome to my Text Game! -----'.upper())
    print(f'You have {lifepoints} life points! ')
    print('\n')
    print('\nYou are on a crossroads...')
    print('Left or Right?')

    answer = input(':').lower()

    if answer == 'left':
        leftside()
    elif answer == 'right':
        rightside()
    else:
        gameover("A car hit you, you can't choose right or left?")

startgame()
