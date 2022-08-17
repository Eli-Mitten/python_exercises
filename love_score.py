
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1.lower() + name2.lower()

decimales = 0
unidades = 0

for x in "true":
	decimales += names.count(x)
for x in "love":
	unidades += names.count(x)
	
score = decimales * 10 + unidades

if score < 10 or score > 90:
	print(name1 + " and " + name2)
	print("Your Love score is " +str(score) +", you go together like coke and mentos.")
elif score > 40 and score < 50:
	print(name1 + " and " + name2)
	print("Your  Love score is " +str(score) +", you are alright together.")
else:
	print(name1 + " and " + name2)
	print("Your Love score is " +str(score) +".")



