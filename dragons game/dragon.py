import random 
import time

def displayIntro():
    print('You are in a land full of dragons. ')
    time.sleep(2)
    print('''Infront of you ,You see two caves.
    In one cave, the dragon is friendly and it will share its treasure with you.
    On the other hand the other dragon is greedy and will eat you on sight''','\n')

    
def chooseCave():
    cave = ""
    while cave !='1' and cave !='2':
        print('Which cave would you go into? (1 or 2)')
        cave = input()
    return  cave

def chekCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('Its dark and spooky....')
    time.sleep(2)
    print('A large dragon jumps infront of you and flaps his jaws open.....')
    print()
    time.sleep(2)


    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure')

    else:
        print('Gobbles you down in a single bite!')