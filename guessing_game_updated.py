import random

def rng_tool(): # RNG tool to get a number between 0 and 100 
	
	random_number = random.randint(0 , 100)

	return random_number

print("Welcome to the Guessing Game of DOOM! Enjoy the cookies!")

correct_number = rng_tool()

running = True

# Game Loop Start
while running:
	x =  input("Enter a Number between 0, and 100: ")
	if  x == ' ' or x == '':
		print("Stop monkeying around and play the game!")
		continue
	elif type(x) == str:
		print("Now you're just being negligent. ")
		x = input("Enter a number between 0 and 100: ")
		continue
	elif int(x) > correct_number:
		print("Too high, guess again.")
		
	elif int(x) < correct_number:
		print("Too low, guess again.")
	else:
		print("Congrats, you win... this time. \n")
		play = input("Play again?: (Y/N) ")
		play.lower()
		if play == 'y':
			correct_number = rng_tool()
		elif play == 'n':
			print("'Til next time.")
			break
		
