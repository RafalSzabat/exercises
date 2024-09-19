#This will be the hangman game

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Please, guess a letter: ").lower()

for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")
