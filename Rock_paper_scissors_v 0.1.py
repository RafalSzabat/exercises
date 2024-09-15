#The goal is to make a simple rock, paper, scissors game without the use of loops, yet.
#Yes, you can input wrong number. This will be updated.

import random
from operator import index

#Taking index input from the player.

index_player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

#making sure the player choice will be an integer

index_player = int(index_player)


#Ascii art for the choices of player and computer.
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
#creating a list of possible choices

possibilities = [rock, paper, scissors]

#Combining player and computer choices from the list

player_choice = possibilities[index_player]
computer_choice = random.choice(possibilities)


#creating possible events and what the result is

if player_choice == rock and computer_choice == paper:
    print(f'{rock}  {paper}  You lose.')
elif player_choice == paper and computer_choice == scissors:
    print(f'{paper}  {scissors}  You lose.')
elif player_choice == scissors and computer_choice == rock:
    print(f'{scissors}  {rock}  You lose.')
elif player_choice == computer_choice:
    print(f'{player_choice} {computer_choice} It\'s a draw.')
else:
    print(f'{player_choice} {computer_choice} Congrats! You win!')
