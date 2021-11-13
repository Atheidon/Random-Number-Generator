import random
lowest_number = int(input("Give the lowest possible number: "))
highest_number = int(input("Give the highest possible number: "))
amount = int(input("Give the amount of random numbers: "))
for i in range(amount): print(random.randrange(lowest_number, highest_number + 1))
