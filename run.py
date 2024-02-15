
import random
import string
import sys
import os
import time
from datetime import datetime, date
name = ''
animals = [
    "dog", "cat", "elephant", "lion", "tiger", "zebra", "giraffe", "hippo",
    "rhino", "cheetah", "monkey", "gorilla", "kangaroo", "koala", "panda",
    "penguin", "bear", "wolf", "fox", "deer", "buffalo", "camel", "gazelle",
    "moose", "elk", "reindeer", "crocodile", "alligator", "snake", "python",
    "cobra", "anaconda", "lizard", "gecko", "iguana", "turtle", "tortoise",
    "frog", "toad", "salamander", "newt", "axolotl", "goldfish", "shark",
    "whale", "dolphin", "octopus", "squid", "jellyfish", "starfish",
    "seahorse", "crab", "lobster", "shrimp", "oyster", "clam", "snail", "slug",
    "bee", "ant", "wasp", "butterfly", "moth", "dragonfly", "grasshopper",
    "cricket", "beetle", "ladybug", "spider", "scorpion", "centipede",
    "millipede", "fly", "mosquito", "caterpillar", "larva", "butterfly",
    "mantis", "armadillo", "anteater", "sloth", "hedgehog", "porcupine",
    "chipmunk", "squirrel", "rabbit", "mouse", "rat", "hamster", "guineapig",
    "gerbil", "ferret", "mole", "weasel", "otter", "badger", "raccoon",
    "skunk", "opossum", "platypus", "echidna"
]
countries = [
    "Brazil", "Japan", "France", "Italy", "Germany", "Canada", "Australia",
    "Mexico", "India", "China", "Spain", "Russia", "Argentina", "SouthAfrica",
    "SouthKorea", "Netherlands", "Switzerland", "Sweden", "Portugal",
    "Belgium", "Norway", "Denmark", "Finland", "Greece", "Egypt", "Turkey",
    "Thailand", "Iran", "Vietnam", "Poland", "Ukraine", "Indonesia",
    "Philippines", "Malaysia", "Israel", "SaudiArabia", "Pakistan",
    "Bangladesh", "Nigeria", "Kenya", "Morocco", "Peru", "Chile", "Colombia",
    "Venezuela", "Cuba", "NewZealand", "Ireland", "Austria", "Hungary"
]
flowers = [
    "rose", "tulip", "daisy", "lily", "sunflower", "orchid", "daffodil",
    "peonies", "hydrangea", "carnation", "poppy", "marigold", "lavender",
    "chrysanthemum", "hibiscus", "gerbera", "snapdragon", "freesia", "iris",
    "aster", "zinnia", "dahlia", "crocus", "azalea", "anemone", "cosmos",
    "lilac", "hyacinth", "geranium", "pansy", "forgetmenot", "bougainvillea",
    "camellia", "ranunculus", "gladiolus", "fuchsia", "birdofparadise",
    "buttercup", "columbine", "delphinium", "foxglove", "gardenia", "larkspur",
    "narcissus", "peony", "sweetpea", "tigerlily", "verbena", "wisteria"
]
languages = [
    "English", "Spanish", "French", "German", "Italian", "Portuguese",
    "Russian", "Japanese", "Chinese", "Arabic", "Hindi", "Bengali", "Urdu",
    "Indonesian", "Korean", "Turkish", "Dutch", "Swedish", "Greek", "Polish",
    "Vietnamese", "Thai", "Finnish", "Norwegian", "Danish", "Romanian",
    "Czech", "Hungarian", "Slovak", "Croatian", "Serbian", "Bulgarian",
    "Ukrainian", "Malay", "Tagalog", "Lithuanian", "Latvian", "Estonian",
    "Albanian", "Slovenian", "Macedonian", "Swahili", "Hausa", "Yoruba",
    "Zulu", "Amharic", "Somali", "Gujarati", "Punjabi"
]
fruits = [
    "apple", "banana", "orange", "grape", "strawberry",
    "watermelon", "blueberry", "mango", "pineapple", "kiwi",
    "peach", "pear", "cherry", "plum", "raspberry",
    "lemon", "lime", "apricot", "coconut", "fig",
    "avocado", "pomegranate", "cantaloupe", "cranberry", "blackberry",
    "guava", "papaya", "lychee", "passionfruit", "date",
    "kiwifruit", "tangerine", "nectarine", "persimmon", "dragonfruit",
    "grapefruit", "mandarin", "boysenberry", "mulberry", "clementine",
    "quince", "plantain", "starfruit", "honeydew", "rhubarb",
    "gooseberry", "soursop", "kumquat", "elderberry", "ackee"
]
categories = {
    "Animals": animals,
    "Countries": countries,
    "Flowers": flowers,
    "Languages": languages,
    "Fruits": fruits
}
levels = {
    "Easy - 8 lives: Perfect for hangman beginners": 8,
    "Hard - 4 lives: For the daring souls who seek a challenge": 4
}


def startup_view():
    # Plays the startup welcome effect with colors and text effects.
    # Welcome message with slow typing effect using txt_effect
    txt_effect("Welcome to The Hangman Madness!\n\n")
    txt_effect("\033[91m"
               f"   ______\n"
               f"  |      |\n"
               f"  |      O\n"
               f"  |     /|\\\n"
               f"  |     / \\\n"
               f"  |\n"
               f"  |\n"
               f"__|_________"
               + "\033[0m\n\n")
    txt_effect("Prepare yourself for an epic journey "
               "through the alphabet jungle.\n\n")
    # Allow time for visual impact
    time.sleep(1.5)
    # Prints the text with a slower typing
    # effect and additional customizations
    # Adjust speed if needed (lower number means slower typing)


def txt_effect(text_to_print):
    for character in text_to_print:
        time.sleep(0.03)
        sys.stdout.write(character)
        sys.stdout.flush()
    # From:
    # https://stackoverflow.com/questions/2084508/clear-terminal-in-python


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_hangman(mistakes, chosen_level):
    hangman_stages = [
        f"   ______\n"
        f"  |      \n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"__|_________ ",
        f"   ______\n"
        f"  |      |\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"__|_________ ",
        f"   ______\n"
        f"  |      |\n"
        f"  |      O\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"__|__________",
        f"   ______\n"
        f"  |      |\n"
        f"  |      O\n"
        f"  |     /\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"__|__________",
        f"   ______\n"
        f"  |      |\n"
        f"  |      O\n"
        f"  |     /|\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"__|__________",
        f"   ______\n"
        f"  |      |\n"
        f"  |      O\n"
        f"  |     /|\\\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"__|__________",
        f"   ______\n"
        f"  |      |\n"
        f"  |      O\n"
        f"  |     /|\\\n"
        f"  |     /\n"
        f"  |\n"
        f"  |\n"
        f"__|__________",
        f"   ______\n"
        f"  |      |\n"
        f"  |      O\n"
        f"  |     /|\\\n"
        f"  |     / \\\n"
        f"  |\n"
        f"  |\n"
        f"__|__________"
    ]
    # Adjust the rate of displaying hangman stages based on the chosen level
    if chosen_level == "Easy - 8 lives: Perfect for hangman beginners":
        display_per_mistake = 1  # Display two stages per mistake
    # Easy level - Display 1 stage per mistake
    # Hard level - Display 2 stage per mistake
    else:
        display_per_mistake = 2
    # Calculate the number of stages to display for the current mistake
    stages_to_display = min(mistakes *
                            display_per_mistake,
                            len(hangman_stages) - 1)
    print("\033[91m" + hangman_stages
          [stages_to_display] + "\033[0m")
    return stages_to_display


def choose_level():
    startup_view()
    name_is_valid = False
    while name_is_valid is False:
        name = get_user_input("What do your friends "
                              "call you?\n")
        clear_terminal()
        name_is_valid = len(name) >= 3
        if name_is_valid is False:
            print("Gimme names, not games!\n")
            print("\033[91mEnter at least 3 letters!\033[0m\n")
    print(f"{name}, thrilled to have you join!\n")
    print("Ready to tackle some challenging words?\n")
    print("Step 1: Choose "
          "Your Level of Adventure!")
    # Yellow decorative line
    print("\033[1;33;40m" + "—" * 39 + "\033[0m\n")
    for i, level in enumerate(levels):
        print(f"{i+1}. {level}")
    while True:
        print(" ")
        choice = input("Enter your level (1-2): ")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(levels):
                chosen_level = list(levels.keys())[choice]
                clear_terminal()
                print("You selected:")
                # Print the chosen category here
                print(chosen_level + ".")
                # Yellow decorative line
                print("\033[1;33;40m" + "—" * 58 + "\033[0m\n")
                print(f"Excellent choice {name}!")
                print(" ")
                # chosen_list refers to a list of words associated
                # with the category that the user has chosen to play with.
                chosen_level_lives = levels[chosen_level]
                return chosen_level, chosen_level_lives, name
            else:
                print(" ")
                print("My circuits are overloaded!")
                print(" ")
                print(f"\033[91m{name}, Please enter \033[0m"
                      "\033[91ma number between 1 and 2.\033[0m")
        else:
            print(" ")
            print("Your character sounds like a dolphin sneeze.")
            print(" ")
            print(f"\033[91m{name}, Please enter a number.\033[0m")


def choose_category(name):
    print("Step 2: Let's explore the world of letters!")
    # Yellow decorative line
    print("\033[1;33;40m" + "—" * 43 + "\033[0m\n")
    print("What is your favorite category?")
    for i, category in enumerate(categories):
        print(f"{i+1}. {category}")
    while True:
        print(" ")
        choice = input("Enter your choice (1-5): ")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(categories):
                clear_terminal()
                chosen_category = list(categories.keys())[choice]
                print("You selected", chosen_category + ".")
                print(" ")
                print("Step 3: Let the guessing game begin!")
                # Yellow decorative line
                print("\033[1;33;40m" + "—" * 36 + "\033[0m\n")
                # Print the chosen category here
                print("On your marks, get set, guess!\n"
                      "The hangman's rope hangs in the balance!")
                # chosen_list refers to a list of words
                # associated with the category that
                # the user has chosen to play with.
                chosen_list = categories[chosen_category]
                return chosen_category, chosen_list
            else:
                print(" ")
                print("I see you're struggling with "
                      "your keyboard skills.")
                print("\033[91mPlease enter a number between 1 and 5.\033[0m")
        else:
            print(" ")
            print("Is that character part of a secret code?")
            print(f"\033[91m{name}, Please \033[0m"
                  "\033[91menter a number.\033[0m")


def chosen_category_word(chosen_list):
    word = random.choice(chosen_list)
    while '-' in word or ' ' in word:
        # randomly choose a word fron the chosen category
        word = random.choice(chosen_list)
    return word.upper()


def get_user_input(prompt):
    return input(prompt)


def hangman():
    chosen_level, chosen_level_lives, name = choose_level()
    chosen_category, chosen_list = choose_category(name)
    word = chosen_category_word(chosen_list)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    mistakes = 0
    while len(word_letters) > 0 and mistakes < chosen_level_lives:
        display_hangman(mistakes, chosen_level)
        print(" ")
        print('You have', chosen_level_lives - mistakes, 'lives left.')
        # Yellow decorative line
        print("\033[1;33;40m" + "—" * 22 + "\033[0m\n")
        word_list = [f'\033[1;36m{letter}\033[0m' if letter in
                     used_letters else '_' for letter in word]
        print('Current word:', ' '.join(word_list))
        print('Used letters:', ' '.join(used_letters))
        print(" ")
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            clear_terminal()
            used_letters.add(user_letter)
            if user_letter in word_letters:
                print("\033[92mThe eagle has landed! \033[0m"
                      "\033[92mOr was it a penguin?\033[0m\n\n"
                      "No matter, you guessed right!")
                word_letters.remove(user_letter)
            else:
                mistakes += 1
                print("\033[91mYikes! Swing and a miss...\033[0m")
        elif user_letter in used_letters:
            clear_terminal()
            print("Oopsie! That letter's already "
                  "been served. Let's order something new!")
        else:
            clear_terminal()
            print(" ")
            print("The keyboard gremlins just ate your character!")
            print(" ")
            print("\033[91mPlease choose a valid \033[0m"
                  "\033[91mone before they attack again.\033[0m")
    if mistakes == chosen_level_lives:
        display_hangman(mistakes, chosen_level)
        print(" ")
        print("Aw, shucks! Looks like your brain "
              "went on vacation with the penguins.")
        print("\033[92mThe word was", word, "\033[0m")
        print(" ")
    else:
        print(" ")
        print("\033[92mThe word was", word, "\033[0m")
        print(" ")
        print("You guessed it!")
        print(" ")
        print("Your detective skills are sharper than\n"
              "Sherlock Holmes on a caffeine bender.")
        print(" ")


def continue_game():
    while True:
        print("Ready for another round?\n\n"
              "It's like potato chips, you can't have just one. (y/n)")
        choice = input().lower()
        if choice == "y":
            # Assuming you have a clear_terminal function defined
            clear_terminal()
            print(" ")
            # Yellow decorative line
            print("\033[1;33;40m" + "—" * 70 + "\033[0m\n")
            print(" ")
            print("Oh good, you haven't given "
                  "up yet. This could get interesting...")
            print(" ")
            while True:
                you_sure = input("Are you sure? (y/n)\n").lower()
                # Check for both "y" and "n"
                if you_sure in ("y", "n"):
                    if you_sure == "y":
                        clear_terminal()
                        # Assuming you have a hangman function defined
                        hangman()
                        # Exit inner loop on confirmation
                        break
                    elif you_sure == "n":
                        print(" ")
                        # Yellow decorative line
                        print("\033[1;33;40m" + "—" * 70 + "\033[0m\n")
                        print(" ")
                        print("Farewell, brave soul! Remember, "
                              "quitting is bravery... sometimes.")
                        print(" ")
                        print("Don't tell my therapist I said that.")
                        print(" ")
                        # Exit the function, effectively ending the game
                        return
                else:
                    print("\033[91mPlease enter \033[0m"
                          "\033[91m'y' or 'n'.\033[0m")
        # Handle "n" from the first prompt directly
        elif choice == "n":
            clear_terminal()
            print(" ")
            print("Thanks for playing!")
            # Yellow decorative line
            print("\033[1;33;40m" + "—" * 19 + "\033[0m\n")
            print(" ")
            print("...and please excuse any existential dread")
            print("you may have experienced during the game.")
            print(" ")
            print("I'm still under development, after all :-)")
            print(" ")
            # Exit the entire loop after farewell message
            break
        else:
            print("Wow, that was... something.")
            print(" ")
            print("Are you trying to speak Morse code?")
            print(" ")
            print("\033[91mPlease enter 'y' or 'n'.\033[0m")
            print(" ")


if __name__ == "__main__":
    hangman()
    continue_game()
