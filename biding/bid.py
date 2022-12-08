# from clear import clear
import os

from time import sleep



bid={}
end_game=False
highest=0
winner=''

def find_highest(highest,winner,bid):
    for b in bid:
        new_bid=bid[b]
        if new_bid>highest:
            highest=new_bid
            winner=b
    print(f"the highest bider is :{winner} and bid is {highest} ")
while not end_game:
    name=input('enter the name of bidder')

    amount=int(input('enter the bid amount'))
    bid[name] = amount
    choose=input('any new bidders (yes/no)')
    if choose=='no':
        end_game=True
        find_highest(highest,winner,bid)

    if choose=='yes':
        sleep(1)
        os.system('cls')
