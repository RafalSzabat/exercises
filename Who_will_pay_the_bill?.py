#Exercise was to create a program that picks a random name from the list.

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_name = random.choice(friends)

print(f"This time the bill will be paid by {random_name}.")
