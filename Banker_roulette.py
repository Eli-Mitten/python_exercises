# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

# numRandom = random.randint(0, len(names) - 1)
paier = random.sample(names, 1)

print(f'{paier[0]} is going to buy the meal today!')
