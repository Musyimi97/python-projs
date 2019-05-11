import random 
number= random.randint(1,10)
tries =1


uname=input("Hello, Whats your name?: ")
print("Hello",uname + ",",)

question = input("Would you like to play a game? [Y/N]: ")
if question=="n":
    print("Oooh.. okay")

if question=="y":
    print("Am thinking of a number between 1 & 10")
    guess = int(input("Have a guess: "))
    if guess >number:
        print("Guess too high..")
if guess<number:
    print("Your number is too low")
while guess != number:
    tries+=1
    guess = int(input("Try again: "))
    if guess < number:
        print("Guess higher")

if guess == number :
    print("Hooray we got a champ!!!, THe number was", number, \
          "and it only took ", tries, "tries!")
