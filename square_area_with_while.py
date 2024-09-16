#Simple area of the square calculator with the use of while loop

#input from the user
if_stop = input("Do you wish to measure the are of square? Y or N ").lower()

#the loop
while if_stop == "y":
    side_of_the_square = input("Side of the square: ")
    area_of_the_square = int(side_of_the_square) ** 2
    print(f'Area of square: {area_of_the_square}')
    if if_stop != "n":
        if_stop = input("Do you wish to continue? Y or N ")
    if if_stop == "n":
        break
print('Program finished.')
