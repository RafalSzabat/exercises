#Password Generator Project
import random

#List of letters, numbers, symbols - I deliberately did not use '()' symbols as they look bad in password aesthetics

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

#Welcome message and inputs from user

print("Welcome to the NewPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#for loops adding random elements to the list

random_password = []
for letter in range(0, nr_letters):
    random_password += random.choice(letters)
for symbol in range(0, nr_symbols):
    random_password += random.choice(symbols)
for number in range(0, nr_numbers):
    random_password += random.choice(numbers)

#Shuffling the list, formatting the list to a string

random.shuffle(random_password)

randomised_password = (''.join(random_password))

#Printing the result

print(f'Your password is: {randomised_password}')
