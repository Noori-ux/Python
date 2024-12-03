import random

numbers = [1,2,3,5,6,7,8,9,10]
print(numbers)

random_numbers=[]

for _ in range(7):
    random_numbers.append(random.randint(0,9))


print(random_numbers)
