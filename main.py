
import random
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


lis=[rock,paper,scissors]
i=0
u_c=0
c_c=0
while i<5:
    inp=int(input('enter your choice 0.rock,1.paper,2.scissor'))
    comp_choice=random.randint(0,3)
    # print(comp_choice)

    if inp==comp_choice:
        print(f"user choice was :{lis[inp]}")
        print(f"computer choice is: {lis[comp_choice]}")
        print('its a draw')
        u_c=1
        c_c=1
    elif inp==0 and comp_choice==1:
        print(f"user choice was :{lis[inp]}")
        print(f"computer choice is: {lis[comp_choice]}")
        print('computer gets point')
        c_c=c_c+1
    elif inp==0 and comp_choice==2:
        print(f"user choice was :{lis[inp]}")
        print(f"computer choice is: {lis[comp_choice]}")
        print('user gets a point')
        u_c = u_c + 1
    elif inp==1  and comp_choice==0:
        print(f"user choice was :{lis[inp]}")
        print(f"computer choice is: {lis[comp_choice]}")
        print('computer gets point')
        c_c = c_c + 1
    elif inp==1  and comp_choice==2:
        print(f"user choice was :{lis[inp]}")
        print(f"computer choice is: {lis[comp_choice]}")
        print('computer gets point')
        c_c = c_c + 1
    elif inp==2  and comp_choice==0:
        print(f"user choice was :{lis[inp]}")
        print(f"computer choice is: {lis[comp_choice]}")
        print('computer gets point')
        c_c = c_c + 1
    elif inp==2  and comp_choice==1:
        print(f"user choice was :{lis[inp]}")
        print(f"computer choice is: {lis[comp_choice]}")
        print('user gets point')
        u_c=u_c+1
    elif inp>2:
        print('invalid option given')
    i=i+1

print(f"'\n'user score = {u_c}")
print(f"comp_score = {c_c}")
if u_c>c_c:
    print('user wins')
elif u_c<c_c:
    print('computer wins')
else:
    print('its a draw')