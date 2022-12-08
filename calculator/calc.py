


def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2


op={
    '1':add,
    '2':sub,
     '3':mul,
     '4':div
}
def calc():
    num1=int(input('enter the first number:'))
    end=False
    while not end:
        ch="""choice the for operation
              1.add
              2.sub
              3.mul
              4.div """
        choice=input(ch+'\n')
        num2=int(input('enter second number:'))
        call=op[choice]
        p=call(num1,num2)
        print(p)
        new_choice=input("do you want to continue with current answer:'y' or start new:'n' ")
        if new_choice=='y':
            num1=p
        if new_choice=='n':
            calc()

calc()
