import random
from words import words

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)    # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    # what the user has guessed

    #getting user input
    while_len(word_letters) > 0:
        # letters used
        print('You have used these letters: ',' '.join(used_letters))

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user:letter in word_letters:
            word_letters.remove(user_lettre)

elif user_letter in used_letters:
    print('You have already used that character. Please try again.')

else:
    print('Invalid character. Please try again.')


hangman()