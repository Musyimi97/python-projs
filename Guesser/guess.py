import random

x = random.randrange(1,100)
user = input('please enter any number:'),
val = int(user)
if val == x:
    print('Jackpot'),
elif x<val:
    print('Number too low')
else:
    print('Your guess is too high')
