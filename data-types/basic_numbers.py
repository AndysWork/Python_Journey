#My First Program#
# name = input("What is your name?")
# print("This is my first Python Script!! & My name is "+ name)

# Python Keywords - True, False, None, continue, del, pass

daily_steps=10000
print(type(daily_steps))

print((5+2)*10)

footsteps = 2000
footsteps += 200
print(footsteps)
footsteps -= 300
print(footsteps)
footsteps *= 2
print(footsteps)

print(69/12) #Gives Actual Result
print(69//12) #Gives Divisor (Nearest home number)
print(69%12) #Remainder

print(8**3) #Exponent Operation

print(1+ 1.0) #Int to Float

print(int(2.8)) #Convert to Int
print(float(2)) #Convert to Float

print(1.1 + 2.2) # 1.1 + 2.2 = 3.3000000000000003

from decimal import Decimal as D
print(D('1.1') + D('2.2') == D('3.3')) #The more the fraction the more precision

import math
print(math.pi)
print(math.factorial(6))

