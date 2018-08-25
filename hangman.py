import os
from hang_man import die
word={'1':['h', 'r', 'y', 'p', 't', 'e'], '2':['i', 'o', 'm', 'a'], '3':['t', 'o'], '4':['d', 's', 't', 'a', 'g'], '5':['w', 't', 'h', 'u', 'e']}
count=0	
def ini():
	print("\n 1\n 2\n 3\n 4\n 5")
	ch=input("choose the word behind nos: ")
	return ch
	
def playAgain():
	choc=input("do you want to play aganin? (Y/N): ")
	if choc=='y':
		comp()

	elif choc=='n':
		os.system("cls") 

	else:
		print("invalid choice!")
		os.system("cls")

def compare(cho):
	for i in range (len(word[cho])):
		letter=input("guess the missing letter: ")	
		if letter in word[cho]:
			print("your guess is correct.")

		else:
			print("sorry, your guess is wrong. please try again ")

			
			
	print("congratulations!!! you have guessed the correct word")
	playAgain()

def comp():
	ch=ini()
	if ch=='1':
		print("_A_R_  _O_T_R ")
		compare(ch)

	elif ch=='2':
		print("_R_N  _ _N")
		compare(ch)

	elif ch=='3':
		print("_H_R")
		compare(ch)

	elif ch=='4':
		print("_R  _ _R_N_E")
		compare(ch)

	elif ch=='5':
		print("_I_C_  	_ _NT_R")
		compare(ch)

	else:
		print("invalid choice!")

comp()
die(4)
