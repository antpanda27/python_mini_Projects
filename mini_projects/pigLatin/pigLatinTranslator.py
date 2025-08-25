from ctypes import pythonapi
import time
import datetime

def pigLatin():
	vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
	piglatword = ''; piglatSentence = []

	sentence = input('Please enter your word or sentence in English \n ↳ ')

	wordlist = sentence.split() # Seperate words within inputted sentence
	for word in wordlist: # Loop through each word
		wordEnd = ''; wordBegin = ''; alnumwordBegin = ''; nonAlnum = ''
		# Collecting consonants and consonants clusters
		if not word.startswith(vowels):
			for x in word.lower():
				if x in vowels:
					break
				else:
					wordEnd += x

			wordBegin = word[int(len(wordEnd)):]

			# Move non-alphanumerical characters to the end
			for c in wordBegin:
				if c.isalnum():
					alnumwordBegin += c
				else:
					nonAlnum += c

			#String it all together into a list to later use ' '.join
			piglatword = alnumwordBegin + wordEnd + 'ay' + nonAlnum
			piglatSentence.append(piglatword)
		# Collecting vowel starting words
		elif word.startswith(vowels):
			piglatword = word.lower() + 'way'
			piglatSentence.append(piglatword)

	# Add in loading animation and dialog before output
	i = 0
	while i < 3:
		i += 1
		print('.', end=''); time.sleep(0.7)
	print(f' \"{sentence}\" in Pig Latin is:')

	print(' '.join(piglatSentence).capitalize(),end = '\n \n')

	# Save translation
	save = open('history.txt', 'a+')
	save.write(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n {sentence} > {' '.join(piglatSentence).capitalize()}\n\n')
	save.close()

print('Welcome to Pig Latin by SkillageIT')

# Program menu
while True:

	welcome = input('(S) Start Translations   (H) View History   (E) Exit \n ↳ ')
	if welcome.upper() == 'S':
		pigLatin()

	# History Menu
	elif welcome.upper() == 'H':
		history = open('history.txt', 'r')
		print(*history.readlines())
		history.close()
		print('...',); time.sleep(0.7)

	# Close option
	elif welcome.upper() == 'E':
		break
	else:
		print('That is not a valid option')
