import random
print('I will flip a coin 1000 times. Guess how many times it will come heads. (Press to begin)')
input()
flips =0
heads =0

while flips < 1000:
    if random.randint(0,1)==1:
        heads +=1