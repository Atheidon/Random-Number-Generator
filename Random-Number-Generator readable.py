#A SIMPLE RANDOM NUMBER GENERATOR, MADE IN PYTHON BY ATHEIDON8
#importing required modules
import random
#asking for the numbers and amount
lowest_number = int(input("Give the lowest possible number: "))
highest_number = int(input("Give the highest possible number: "))
amount = int(input("Give the amount of random numbers: "))
#the actual number generator function: it's what generates the numbers
for i in range(amount): 
    print(random.randrange(lowest_number, highest_number + 1))
input("press enter to exit")