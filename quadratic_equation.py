from math import sqrt


a = float(input('Value of a: '))
b = float(input('Value of b: '))
c = float(input('Value of c: '))

x = ((-b) + sqrt(b**2-4*a*c))/(2*a)
x2 = ((-b) - sqrt(b**2-4*a*c))/(2*a)
print(f'The roots are {x} and {x2}')
