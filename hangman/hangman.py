
import random
from hangman_logo import logo
from words import words

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_game=False
# words=['danger','john','eat']
choosen_word=random.choice(words)
print(choosen_word)
length=len(choosen_word)
strings=[]
lives=6
for len in range(length):
    strings.append('_')

print(logo)
while not end_game:
    guess=input('guess an alphabet')
    for i in range(length):
        choose=choosen_word[i]
        if guess==choose:
            strings[i]=guess
    print(f"{''.join(strings)}")        # joins the list of words
        # print(strings)
    if guess not in choosen_word:
        lives-=1
        if lives==0:
            print('you loose')
            print(stages[lives])
            end_game=True
    if '_' not in strings:
       print('you win the game')
       end_game=True

    print(stages[lives])