import os
from hang_man import die
word={'1':['h', 'r', 'y', 'p', 't', 'e'], '2':['i', 'o', 'm', 'a'], '3':['t', 'o'], '4':['d', 's', 't', 'a', 'g'], '5':['w', 't', 'h', 'u', 'e']}

def ini():
	print("\n 1\n 2\n 3\n 4\n 5")
	ch=input("choose the word behind nos: ")
	return ch #stores the no 
	
def playAgain():
	choc=input("do you want to play aganin? (Y/N): ")#stores yes or no opt
	if choc=='y':
		comp()

	elif choc=='n':
		os.system("cls") 

	else:
		print("invalid choice!")
		os.system("cls")

def compare(cho):
	wcount=0
	rcount=0
	length=len(word[cho])
	print(length)
	for i in range (len(word[cho])+4): #stores value in ch
		letter=input("guess the missing letter: ")	
		if rcount<length and letter in word[cho] :
			rcount+=1
			print("your guess is correct.")

		if letter not in word[cho] and wcount<=4 :
			wcount+=1
			die(wcount)

		if rcount==length:
			print("congratulations!!! you have guessed the correct word")
			playAgain()
		
		if wcount>4:
			print("OOPS!! You have lost your chances")
			input("press any key: ")
			os.system("cls")
			exit()

			
	
def comp():
	choose=ini()
	if choose=='1':
		print("_A_R_  _O_T_R ")
		compare(choose)

	elif choose=='2':
		print("_R_N  _ _N")
		compare(choose)

	elif choose=='3':
		print("_H_R")
		compare(choose)

	elif choose=='4':
		print("_R  _ _R_N_E")
		compare(choose)

	elif choose=='5':
		print("_I_C_  	_ _NT_R")
		compare(choose)

	else:
		print("invalid choice!")

comp()

