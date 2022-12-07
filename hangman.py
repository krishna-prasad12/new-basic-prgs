import random
import string

words=['camel','dragon','tortoise']
rands=random.choice(words)
emp=[]
print(f'correct word is {rands}')
lens=len(rands)
for len in range(lens):
    emp.append('_')   # print lines for each of aphabet of random word
print(emp)

user_input=input('guess a alphabet of the word').lower()
for rand in rands:
    if rand==user_input:
        new = rands.index(rand)
        emp[new]=user_input
print(new)
print(emp)
