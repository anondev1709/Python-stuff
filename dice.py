#### Mini project game for dice rolling simulator ####

from random import randint

#### 

def dice():
	while True:
		dice_val = randint(1, 6)
		print("You throw the dice and the number is " + str(dice_val))
		if dice_val == 6:
			print("Congratulations! You won! Do you wish to try again?")
			p = input("> ")
		else:
			print(f"Well {dice_val} is not much, do you want to try again?")
			p = input("> ")
		if p == "yes":
			continue
		else:
			print("Thank you for playing!")
			return 

dice()