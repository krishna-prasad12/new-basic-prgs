import random


def rand_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card



def compare(user_score,comp_score):
    if user_score==comp_score:
        return 'draw'
    elif comp_score==0:
        return 'you loose opponent has blackjack'
    elif user_score==0:
        return'you win with blackjack'
    elif user_score>21:
        return'you went over you loose'
    elif comp_score>21:
        return'opponent went over you win'
    elif user_score>comp_score:
        return'you win'

def cal_score(user_card):
    if sum(user_card)==21 and len(user_card)==2:
      return 0
    elif 11 in user_card and sum(user_card)>21:
        user_card.remove(11)
        user_card.append(1)
        return sum(user_card)
    else:
        return sum(user_card)

def play_game():
    user_card=[]
    dealer_card=[]
    for i in range(2):
        user_card.append(rand_card())
        dealer_card.append(rand_card())
    game_over=False
    while not game_over:
        user_score=cal_score(user_card)
        comp_score=cal_score(dealer_card)
        print(f'your cards are:{user_card}and score:{user_score}')
        print(f'computer first card is:{dealer_card[0]}')
        if user_score==0 or comp_score==0 or user_score>21:
            game_over=True
        else:
            user_input=input('do you want to hit or hold (y/n)')
            if user_input=='y':
                user_card.append(rand_card())
            else:
                game_over=True

    while comp_score!=0 and comp_score<17:
        dealer_card.append(rand_card())
        print(dealer_card)
        comp_score=cal_score(dealer_card)
    print(f"   Your final hand: {user_card}, final score: {user_score}")
    print(f"   Computer's final hand: {dealer_card}, final score: {comp_score}")

    print(compare(user_score,comp_score))

while input('do you want to play (y/n)') =='y':
    play_game()



