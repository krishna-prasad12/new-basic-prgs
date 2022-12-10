from data import resources,MENU


def inputs(choice):
    if choice=='report':
        print(f"water:{resources['water']}")
        print(f"milk:{resources['milk']}")
        print(f"coffee:{resources['coffee']}")
    elif choice=='off':
        exit()
    else:
        p=resource(choice)
        return p

def resource(choice):

    for item in resources:
        # print(resources[item])
        # print(MENU[choice][item])
        if MENU[choice]['ingredients'][item]>resources[item]:
            print(f'There is not enough of {item}')
            return False
    return True

    # if choice=='expresso':
    #    if resources['water']>=50 and  resources['coffee']>=18:
    #        return 'yes'
    #    else:
    #        print('not enough resources in machine')
    # elif choice=='latte':
    #    if resources['water']>=200 and resources['milk']>=150 and  resources['coffee']>=24:
    #        return 'yes'
    #    else:
    #        print('not enough resources in machine')
    # elif choice=='cappuccino':
    #    if resources['water'] >= 250 and resources['milk'] >= 100 and resources['coffee'] >= 24:
    #        return 'yes'
    #    else:
    #        print('not enough resources in machine')
    #        exit()

def process_coins(quarter,dimes,nickel,penny,choice):
    tot_amount=quarter*0.25+dimes*0.10+nickel*0.05+penny*0.01
    tot_amount=round(tot_amount,2)
    profit=0
    for i in MENU:
      if i==choice:
        if tot_amount==MENU[i]['cost']:
            profit = profit +MENU[i]['cost']
            make_cofee(choice,profit)

        elif tot_amount>MENU[i]['cost']:
            bal=tot_amount-MENU[i]['cost']
            print(f'collect the balance amount:{bal}$')
            profit =profit +MENU[i]['cost']
            make_cofee(choice,profit)
        else:
            print("Sorry that's not enough money.")


def make_cofee(choice,profit):
    resources['Money']=profit
    for i in MENU:
        if i==choice:
            resources['water']-=MENU[i]['ingredients']['water']
            resources['milk'] -= MENU[i]['ingredients']['milk']
            resources['coffee'] -= MENU[i]['ingredients']['coffee']
    print(f'Here is your {choice} enjoy!')



while True:
    menu=f"what would you like? (espresso/latte/cappuccino):"
    choice=input(menu)
    p=inputs(choice)
    if p:
        quarter = float(input('enter amount of quarters:'))
        dimes = float(input('enter amount of dimes:'))
        nickel = float(input('enter amount of nickel'))
        penny = float(input('enter amount of pennies:'))
        process_coins(quarter,dimes,nickel,penny,choice)
