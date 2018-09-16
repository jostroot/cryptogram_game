# This is a game where you are presented with a cryptogram chosen randomly by
# the program. To solve you must enter a letter of the cryptogram and then the letter
# you think it is. If you are correct, the puzzle is reprinted with the correct letters,
# wherever they occur, replacing blanks.

# Import the list of quotes from quotes.txt
with open('quotes.txt') as file_object:
	q_list = []
	for line in file_object:
		qt = line.rstrip('\n')
		q_list.append(qt)
	quote_list = q_list

# define variables
play_again = 'Y'
numq = len(quote_list)

# define the functions

def get_quote():
	"""
	returns a random quote from the quote list
	"""
	from random import randint
	num = randint(0,(numq-1))
	return quote_list[num]

def get_solution(arg1, arg2):
	"""
	creates the solution_list for the solution (all the blanks that get filled in)
	arg1 is the alpha variable, a list of the alphabet in capital letters
	arg2 is the list of coded letters from the chosen quote, aka 'puzzle_list'
	"""
	sltn_list = []
	lngt = len(arg2)
	for n in range(0,lngt):
		if arg2[n] in arg1:
			sltn_list.append('_')
		else:
			sltn_list.append(arg2[n])
	return sltn_list

def get_ciphercode(arg):
	"""
	Creates the cipher code 
	"""
	from random import shuffle
	x = arg
	shuffle(x)
	return "".join(x)

def code_this(arg1,arg2):
	"""	 
	# translate quote into ciphertext. in maketrans the first arg is the target 
	# code, the second arg is what you're translating from.
	arg1 is the quote
	arg2 is the ciphercode
	"""
	arg1 = arg1.upper()
	coded_sentence = arg1.translate(str.maketrans(arg2,'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	return coded_sentence

def get_letterlist(arg):
	"""
	returns the puzzle_list
	"""
	return [x for x in arg]

# play again loop
while play_again == 'Y':
	# define the default alphabet list
	alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
	'R','S','T','U','V','W','X','Y','Z']
	wrong_guess = 0
	# get the random quote
	quote = get_quote()
	
	# create and validate the key codes needed (some of this will be commented out  

	alphacode = "".join(alpha)
	still_need_a_code = True

	while still_need_a_code == True:

		ciphercode = get_ciphercode(alpha)
		code_is_bad = False

		# Test code to make sure no letters match their code (never have a=a, for ex.)
		for n in range(0,26):
			if alphacode[n] != ciphercode[n]:
				continue
			else:
				code_is_bad = True
				break

		if code_is_bad == True:
			print('getting puzzle...\n')
		else:
			still_need_a_code = False
				
	# change the quote to code
	puzzle = code_this(quote, ciphercode)

	# convert the quote into the key, puzzle and solution lists
	quote = quote.upper()
	key_list = get_letterlist(quote)
	puzzle_list = get_letterlist(puzzle)
	solution_list = get_solution(alpha, puzzle_list)

	# print the puzzle and ask for input
	print("\nWelcome to the game! Here's your cryptogram:\n")
	print("".join(puzzle_list))
	print("".join(solution_list))
	# print("".join(key_list))

	# elicit and test the input; test for win
	# need to use alphacode and cipher to test
	# the list in alpha order is actually the code
	solved = False
	while solved == False:
		code_letter = input(str('Code letter? : ')).upper()
		real_letter = input(str('Real letter? : ')).upper()
		uncoded_letter = code_letter.translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', ciphercode))

		if uncoded_letter == real_letter:
			print('Right you are!')

			#HERE IS WHERE YOU UPDATE solution_list
			for n in range(0,len(puzzle_list)):
				if puzzle_list[n] == code_letter:
					solution_list[n] = uncoded_letter

			#PRINT PUZZLE AND UPDATED SOLUTION
			print()
			print("".join(puzzle_list))
			print("".join(solution_list))
			# print("".join(key_list))
		else:
			print('\nNope. Guess again.\n')
			wrong_guess = wrong_guess + 1

		#HERE IS WHERE YOU TEST TO SEE IF IT'S SOLVED
		#IF SO, CONGRATULATE THE WIN!
		if key_list == solution_list:
			solved = True
			print('You have won! Congratulations!')
			print(f'You had {wrong_guess} wrong guesses.')

	# ask to play again
	play_again = (input(str('\nWould you like to play again? (Y for yes) '))).upper()

print('\nThank you for playing and have a nice day!\n')