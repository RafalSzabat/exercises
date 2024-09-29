''' This is an entry level exercise on conditional statements from Python MOOC 2024, I wanted to share it just because I am pretty proud of the unorthodox solution I came up with :D 
Please write a program which asks for the user's name. If the name is anything but "Jerry",
the program then asks for the number of portions and prints out the total cost. The price of a single portion is 5.90.

Two examples of the program's execution:

Sample output
Please tell me your name: Kramer
How many portions of soup? 2
The total cost is 11.8
Next please!

Sample output
Please tell me your name: Jerry
Next please!
'''
# Some out of the box solution I guess :)
# Write your solution here

name = input('Please tell me your name: ')

if name != 'Jerry':
    soup = int(input("How many portions of soup? "))
    print(f'The total cost is {(soup * 5.9):.2f}')
    print('Next please!')
else:
    print('Next please!')
