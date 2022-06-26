import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

weapon = [rock,paper,scissors]

my_choice = int(input('Your choice of weapon. 0 for rock, 1 for paper, 2 for scissors:\n'))
if my_choice == 0:
    print(f'\nYou have chosen:{weapon[0]}')
elif my_choice == 1:
    print(f'\nYou have chosen:{weapon[1]}')
elif my_choice == 2:
    print(f'\nYou have chosen:{weapon[2]}')
else:
    print('Your choice is invalid. Please try again...')

# computer_choice = random.choice(weapon)
# print(f'Computer has chosen:{computer_choice}')
computer_choice = random.randint(0,2)
print(f'Computer has chosen:{weapon[computer_choice]}')

if my_choice == 0 and computer_choice == 2:
    print('You win!')
elif computer_choice == 0 and my_choice == 2:
    print('You lose!')
elif my_choice > computer_choice:
    print('You win!')
elif computer_choice > my_choice:
    print('You lose!')
else:
    print('Draw!')



