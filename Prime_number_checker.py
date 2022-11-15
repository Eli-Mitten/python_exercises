number = int(input("Insert number"))

if number > 1:
	is_prime = True
	
	for num in range(1, number):
		if number % num == 0:
			is_prime = False
			break

if is_prime:
	"Es un numeo primo"
else:
	"No es un numero primo"