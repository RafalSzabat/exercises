#Password Generator Project
import random

#List of letters, numbers, symbols - I deliberately did not use '()' symbols as they look bad in password aesthetics

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

#Welcome message and input from user

print("Welcome to the NewPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#for loops adding random elements to lists

random_letter = []
for letter in range(0, nr_letters):
    random_letter += random.choice(letters)
random_symbol = []
for symbol in range(0, nr_symbols):
    random_symbol += random.choice(symbols)
random_number = []
for number in range(0, nr_symbols):
    random_number += random.choice(numbers)

#Adding the lists, shuffling them, and joining to create a password

password = random_letter + random_symbol + random_number
random.shuffle(password)
randomised_password = (''.join(password))

#printing the result

print(f'Your password is: {randomised_password}')
