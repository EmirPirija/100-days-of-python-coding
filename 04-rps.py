rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game_image = [rock, paper, scissors]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n'))
if user_choice >= 3 or user_choice < 0:
  print('Invalid number. Please try again!')
else:
  print(game_image[user_choice])

computer_choice = random.randint(0, 2)
print('Computer chose: ')
print(game_image[computer_choice])

if (user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0):
  print('You win')
elif user_choice == computer_choice:
  print('DRAW. Try again!')
else:
  print(f'You lost! The computer chose, {computer_choice}')

# user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n'))
# print(game_image[user_choice])

# computer_choice = random.randint(0, 2)
# print('Computer chose: ')
# print(game_image[computer_choice])