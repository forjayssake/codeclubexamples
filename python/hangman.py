from random import random
import os

"""
	SIMPLE HANGMAN
	
	improvements 
	- check for fails == 0 before building scaffold
	- letter does not need non-blank value before checking in is_letter()
	- fixed issue where user could enter non-numeric for number of players, causing error
	- show the full word if player fails to guess it in time
	- added `play again` option
	- update display of word on successful guessing of the word
	- clear the terminal on each guess, and on other decision points
	- prevent user entering word with non-alpha character
	
	possible improvements
	- difficulty level
	- phrase hangman
	- guess whole word
	- show guessed letters
	- refactor start_guessing() - it's a mess
	- customised win/lose message based on the number of fails/letters remaining
	- prevent the same word occuring concurrently
"""

def init_game(difficultyLevel = 1):
	
	# not sure what to do with this yet, but could:
	# * change the constraints on min/max word length
	# * pre-populate X letters in the word
	difficulty 	= difficultyLevel
	
	word  		= ''
	max_length	= 10
	min_length	= 3
	max_fails	= 10
	
	# `2 player` just means you get to enter your own word
	players = int(get_players());
	
	if (players == 2):
		word = get_player_one_word(min_length, max_length)
	else:
		word = get_word_from_list()
	
	start_guessing(max_fails, word.upper())
	


def get_players():
	"""
		return a number of players between 1 and 2
	"""
	players = 0
	while players not in [1,"1", 2, "2"]:	
		players = input('Enter number of players 1 or 2? ')
		if (players not in [1,"1", 2, "2"]):
			print('A value of 1 or 2 must be entered')
	
	return int(players)

	

def get_player_one_word(min, max):
	"""
		return a user defined word of between min and max characters
	"""
	word_valid = False
	while word_valid == False:
	
		text = 'Player 1, enter a word (between ' + str(min) + ' and ' + str(max) + ' characters): '
		word = input(text)
		
		if len(word) < min or len(word) > max:
			print('Word must be between', min, 'and', max, 'characters')
		elif not is_alpha(word):
			print('Word must consist of LETTERS only!')
		else:
			word_valid = True
	
	return word;



def get_word_from_list():
	"""
		return a random word from the list of available hangman words
	"""
	words = open('hangman_words.txt', 'r').readlines()
	return choose(words).strip()


	
def choose(L):
	"""
		given a list L return a random element from it
	"""
	element = random()
	element = int(element*len(L))
	
	return L[element]

	

def start_guessing(max_fails, word):
	"""
		accept user input of letters and display results
	"""
	fails = 0
	word_list = list(word.upper())
	found_letters = []
	
	clear_display()
	
	update_result_display(word, found_letters)	# set the initial display
	
	while fails < max_fails:
	
		letter = fetch_letter()
		
		clear_display()
		
		if check_letter_in_word(letter, word_list):
			
			print('Good Guess!')
			
			# remove the matching letter(s) from word_list
			while letter in word_list:
				word_list.remove(letter)
			
			found_letters.append(letter) # add letter to the list of found letters
			
			if len(word_list) == 0:
				build_scaffold(fails)
				update_result_display(word, found_letters)
				print('Yay! Correct! And in the `neck` of time...')
				play_again()
				return
		else:
			print('Nope...')
			fails = fails + 1
		
		build_scaffold(fails)
		# display the word with correctly guessed letters shown
		update_result_display(word, found_letters)
			
	# end condition
	print('Too bad you loose. The word was ' + word + '. Better luck `necks` time...')
	play_again()
	
 
def play_again():
	"""
		restart game if user inputs 'y'
	"""
	choice = ''
	while choice.lower() not in ['y', 'n']:
		choice = input('Play again? (y/n): ')
	
	if (choice.lower() == 'y'):
		clear_display()
		init_game()
	
	return;
 


def clear_display():
	"""
		clear the terminal
	"""
	os.system('cls' if os.name == 'nt' else 'clear')



def fetch_letter():
	"""
		return a user entered letter
		ensure enter character is alpha
	"""
	letter = ''
	while not is_letter(letter):
		letter = input('Enter a letter (a - z): ')
	
	return letter.upper()



def build_scaffold(fails):
	"""
		print out the relevant parts of the scaffold 
		for the number of failed attempts
	"""
	
	if fails < 1:
		return
	
	scaffold_frame = [
		"/--\\",
		" |",
		" |",
		" |",
		" |",
		" |",
		" |------",
	]
	
	man  = [
		" |     O",
		" |    /|\\",
		" |    / \\",
	]
	
	pieces = []
	frame 	= len(scaffold_frame)
	
	if fails <= frame:
		for n in range(fails):
			pieces.append(scaffold_frame[n])
	else:
		pieces = pieces + scaffold_frame
	
	if fails> frame:
		if fails == 8:
			pieces[5] = man[0]
		elif fails == 9:
			pieces[5] = man[0]
			pieces[4] = man[1]
		else:
			pieces[5] = man[0]
			pieces[4] = man[1]
			pieces[3] = man[2]
	
	pieces.reverse()
	for bit in pieces:
		print(bit)



def update_result_display(word, found_letters):
	"""
		print the hangman word with * for unguessed letters
	"""
	display = []
	for letter in (word):
		if letter in found_letters:
			display.append(letter.upper())
		else:
			display.append('*')
	
	print(''.join(display))



def check_letter_in_word(letter, word_list):
	"""
		return whether a given letter appears in a given word
	"""
	return letter.upper() in word_list




def is_alpha(word):
	"""
		determine whether a given word consists only of alpha characters
	"""
	for character in word:
		if is_letter(character) == False:
			return False
			
	return True



def is_letter(character):
	"""
		return whether a given character is A-Z or a-z
	"""
	if len(character) == 1:
		ascii = ord(character)
		if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
			return True
	
	return False

	
	
if __name__ == '__main__':
	init_game()
