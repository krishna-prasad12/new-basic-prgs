import random
import string

words=['camel','dragon','tortoise']
rands=random.choice(words)
emp=[]
print(f'correct word is {rands}')
lens=len(rands)
emp.append('_'*lens)   # print lines for each of aphabet of random word
print(emp)

user_input=input('guess a alphabet of the word').lower()
for rand in rands:
    new=int(rands.index(rand))
    print(new)
    if rand==user_input:
        emp[0][new]=user_input

