import random
from art import art


def call_run(rand,no):
    for i in range(no):
        print(f'you have {no} attempts remaining ')
        guess = int(input('Guess the number:'))
        if rand == guess:
            print('Your guess is correct')
            return no
            break
        elif guess > rand:
            no-=1
            print('your guess is high')
            print('Guess again')

        elif guess < rand:
            no-=1
            print('your guess is low')
            print('Guess again')
    if no==0:
        print('You loose! you have run out of attempts')
        return no


def call_play():
    print(art)
    print('Welcome to the Number Guessing Game')
    print("I'm Thinking of a number between 1 and 100")
    choice=input('Choose the difficulty: easy or hard:')
    rand=random.randint(1,100)
    print(rand)
    if choice=='hard':
       no= call_run(rand,5)
       return no
    if choice=='easy':
        no=call_run(rand,10)
        return no
p=call_play()
if p==0:
    while input('Do you want to try again(y/n):')=='y':
        call_play()