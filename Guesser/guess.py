import random

x = random.randrange(1,100)
user = int(raw_input('please enter any number:')),
if user == x:
    print('Jackpot'),
elif x<user:
    print('Number too low')
else:
    print('Your guess is too high')
