import random
import logging

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')


guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug(guess)
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('before translation :' + str(toss))
if toss == 0:
    toss = 'tails'
elif toss == 1:
    toss = 'heads'
logging.debug('after translation :' + toss)
if toss == guess:
    print('You got it!')
else:   
    print('Nope! Guess again!')
    guess = input()
    logging.debug(toss)
    if toss == guess:
      
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

