import hangman_art
import hangman_words
import random

print(hangman_art.logo)
print()
print(hangman_art.dashed_line)

chosen_word = random.choice(hangman_words.word_list)
chosen_word_list = []
for i in range(len(chosen_word)):
	chosen_word_list.append("_")

lives_left = 6

while True:
	print()
	for i in chosen_word_list:
		print(i, " ", end='')

	print()
	print(hangman_art.stages[lives_left])
	user_guess = input("Choose the letter: ").casefold()

	list_index = 0
	letter_guessed = False
	for letter in chosen_word:
		if letter == user_guess:
			chosen_word_list[list_index] = letter.upper()
			letter_guessed = True
		list_index += 1

	if not letter_guessed:
		lives_left -= 1

	if lives_left == 0:
		print(hangman_art.dashed_line)
		print(hangman_art.stages[lives_left])
		print("The correct answer is {}.".format(chosen_word.upper()))
		print("GAME OVER. You lose.")
		break
	elif "_" not in chosen_word_list:
		print()
		print(hangman_art.dashed_line)
		print("You guessed! The answer is {}.".format(chosen_word.upper()))
		print("GAME OVER! You win!")
		break
