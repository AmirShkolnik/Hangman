import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)    # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    # what the user has guessed

    lives = 6 # Define lives as a global variable
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b',  'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters:', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1  # takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')


def continue_game():
    play_game = True
    while play_game:
        continue_playing = input("Would you like to continue playing the game? y/n ")
        
        if continue_playing.lower() == "y":
            print("You have decided to continue playing the game.")
            hangman() # restart the game if user chooses to continue
        elif continue_playing.lower() == "n":
            print("Now closing the game...")
            play_game = False
        else:
            print("That is not a valid option. Please try again.")

    print("Thanks for playing")


hangman()
continue_game()
