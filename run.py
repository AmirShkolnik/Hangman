import colorama
import random
import string
import sys
import os
import time
from datetime import datetime, date
from colorama import init
from colorama import Fore, Style
name = ''

animals = [
    "dog", "cat", "elephant", "lion", "tiger", "zebra", "giraffe", "hippo", "rhino", "cheetah",
    "monkey", "gorilla", "kangaroo", "koala", "panda", "penguin", "bear", "wolf", "fox", "deer",
    "buffalo", "camel", "gazelle", "moose", "elk", "reindeer", "crocodile", "alligator", "snake", "python",
    "cobra", "anaconda", "lizard", "gecko", "iguana", "turtle", "tortoise", "frog", "toad", "salamander",
    "newt", "axolotl", "goldfish", "shark", "whale", "dolphin", "octopus", "squid", "jellyfish", "starfish",
    "seahorse", "crab", "lobster", "shrimp", "oyster", "clam", "snail", "slug", "bee", "ant", "wasp",
    "butterfly", "moth", "dragonfly", "grasshopper", "cricket", "beetle", "ladybug", "spider", "scorpion",
    "centipede", "millipede", "fly", "mosquito", "caterpillar", "larva", "butterfly", "mantis",
    "armadillo", "anteater", "sloth", "hedgehog", "porcupine", "chipmunk", "squirrel", "rabbit", "mouse",
    "rat", "hamster", "guineapig", "gerbil", "ferret", "mole", "weasel", "otter", "badger", "raccoon",
    "skunk", "opossum", "platypus", "echidna"
]

countries = [
        "Brazil", "Japan", "France", "Italy", "Germany", "Canada", "Australia", "Mexico", "India", "China",
        "Spain", "Russia", "Argentina", "SouthAfrica", "SouthKorea", "Netherlands", "Switzerland", "Sweden",
        "Portugal", "Belgium", "Norway", "Denmark", "Finland", "Greece", "Egypt", "Turkey", "Thailand", "Iran",
        "Vietnam", "Poland", "Ukraine", "Indonesia", "Philippines", "Malaysia", "Israel", "SaudiArabia",
        "Pakistan", "Bangladesh", "Nigeria", "Kenya", "Morocco", "Peru", "Chile", "Colombia", "Venezuela",
        "Cuba", "NewZealand", "Ireland", "Austria", "Hungary"
]

flowers = [
    "rose", "tulip", "daisy", "lily", "sunflower", "orchid", "daffodil", "peonies", "hydrangea", "carnation",
    "poppy", "marigold", "lavender", "chrysanthemum", "hibiscus", "gerbera", "snapdragon", "freesia", "iris",
    "aster", "zinnia", "dahlia", "crocus", "azalea", "anemone", "cosmos", "lilac", "hyacinth", "geranium",
    "pansy", "forgetmenot", "bougainvillea", "camellia", "ranunculus", "gladiolus", "fuchsia", "birdofparadise",
    "buttercup", "columbine", "delphinium", "foxglove", "gardenia", "larkspur", "narcissus", "peony",
    "sweetpea", "tigerlily", "verbena", "wisteria"
]

languages = [
    "English", "Spanish", "French", "German", "Italian",
    "Portuguese", "Russian", "Japanese", "Chinese", "Arabic",
    "Hindi", "Bengali", "Urdu", "Indonesian", "Korean",
    "Turkish", "Dutch", "Swedish", "Greek", "Polish",
    "Vietnamese", "Thai", "Finnish", "Norwegian", "Danish",
    "Romanian", "Czech", "Hungarian", "Slovak", "Croatian",
    "Serbian", "Bulgarian", "Ukrainian", "Malay", "Tagalog",
    "Lithuanian", "Latvian", "Estonian", "Albanian", "Slovenian",
    "Macedonian", "Swahili", "Hausa", "Yoruba", "Zulu",
    "Amharic", "Somali", "Gujarati", "Punjabi"
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
    """
    Plays the startup welcome effect with colors and text effects.
    """
    colorama.init()  # Initialize colorama
    # Welcome message with slow typing effect using txt_effect
    print(Fore.CYAN + "—" * 74 + "\n") # Blue decorative line
    txt_effect(Fore.WHITE + "Welcome to Hangman Madness!\n\n")
    txt_effect(Fore.WHITE + "Prepare yourself for an epic journey through the alphabet jungle.\n\n")
    print(Fore.CYAN + "—" * 74 + "\n\n")  # Blue decorative line
    time.sleep(1.5)  # Allow time for visual impact
    colorama.deinit()  # Deinitialize colorama

def txt_effect(text_to_print):
    """
    Prints the text with a slower typing effect and additional customizations.
    """
    # Consider using a more advanced library like "rich" for complex effects
    for character in text_to_print:
        # Adjust speed if needed (lower number means slower typing)
        time.sleep(0.03)
        sys.stdout.write(character)
        sys.stdout.flush()

def clear_terminal():
    """
    Clears the terminal.
    """
    # From:
    # https://stackoverflow.com/questions/2084508/clear-terminal-in-python

    os.system('cls' if os.name == 'nt' else 'clear')

def display_hangman(mistakes, chosen_level):
    hangman_stages = [
        "",
        "      _____ \n     |      \n     |      \n     |      \n     |      \n     |      \n     |      \n   __|_________      ",
        "      _____  \n     |     | \n     |       \n     |       \n     |       \n     |       \n     |       \n   __|_________ ",
        "      _____ \n     |     | \n     |     O \n     |       \n     |       \n     |       \n     |       \n   __|_________ ",
        "      _____   \n     |     |  \n     |     O  \n     |     |  \n     |        \n     |        \n     |        \n   __|_________ ",
        "      _____   \n     |     |  \n     |     O  \n     |    /|  \n     |        \n     |        \n     |        \n   __|_________ ",
        "      _____   \n     |     |  \n     |     O  \n     |    /|\\ \n     |        \n     |        \n     |        \n   __|_________ ",
        "      _____    \n     |     |  \n     |     O  \n     |    /|\\ \n     |    /   \n     |        \n     |        \n   __|_________ ",
        "      _____    \n     |     |  \n     |     O  \n     |    /|\\ \n     |    / \\ \n     |        \n     |        \n   __|_________ "
    ]
    
    # Adjust the rate of displaying hangman stages based on the chosen level
    if chosen_level == "Easy - 8 lives: Perfect for hangman beginners":
        display_per_mistake = 1  # Display two stages per mistake
    else:  # Easy level
        display_per_mistake = 2  # Hard level  # Display one stage per mistake
    
    # Calculate the number of stages to display for the current mistake
    stages_to_display = min(mistakes * display_per_mistake, len(hangman_stages) - 1)
    
    print(Fore.RED + hangman_stages[stages_to_display] + Style.RESET_ALL)
    return stages_to_display

def choose_level():
    startup_view()
    name_is_valid = False
    while name_is_valid is False:
        name = get_user_input(Fore.WHITE + "What do your friends call you? \n" + Style.RESET_ALL)
        clear_terminal()
        name_is_valid = len(name) >= 3
        if name_is_valid is False:
            print(Fore.RED + "Please enter at least 3 letters for your username" + Style.RESET_ALL)
            print(" ")
    print(f"{name}, thrilled to have you join!")
    print("Ready to tackle some challenging words?")
    print(" ")
    print(Fore.WHITE + "Step 1: Choose Your Level of Adventure!" + Style.RESET_ALL)
    print(Fore.CYAN + "—" * 39 + Style.RESET_ALL)  # Blue decorative line
    for i, level in enumerate(levels):
        print(f"{i+1}. {level}")

    while True:
        print(" ")
        choice = input("Enter your level (1-2): \n")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(levels):
                chosen_level = list(levels.keys())[choice]
                clear_terminal()
                print("You selected:")
                print(Fore.CYAN + "—" * 13 + Style.RESET_ALL) 
                print(chosen_level + ".")  # Print the chosen category here
                print(" ")
                print(f"Excellent choice {name}!")
                print(" ")
                chosen_level_lives = levels[chosen_level]  # chosen_list refers to a list of words associated with the category that the user has chosen to play with.
                return chosen_level, chosen_level_lives, name
            else:
                print(" ")
                print("My circuits are overloaded!")
                print(" ")
                print(Fore.RED + f"{name}, Please enter a number between 1 and 2." + Style.RESET_ALL)
        else:
            print(" ")
            print("Your character sounds like a dolphin sneeze.")
            print(" ")
            print(Fore.RED + f"{name}, Please enter a number." + Style.RESET_ALL)

def choose_category(name):
    print("Step 2: Let's explore the world of letters!")
    print(" ")
    print("What is your favorite category?")
    print(Fore.CYAN + "—" * 30 + Style.RESET_ALL)  # Blue decorative line
    for i, category in enumerate(categories):
        print(f"{i+1}. {category}")

    while True:
        print (" ")
        choice = input("Enter your choice (1-5): \n")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(categories):
                clear_terminal()
                chosen_category = list(categories.keys())[choice]
                print("You selected", chosen_category + ".")
                print(" ")
                print("Step 3: Let the guessing game begin!")
                print(Fore.CYAN + "—" * 36 + Style.RESET_ALL ) # Blue decorative line
                print("On your marks, get set, guess! The hangman's rope hangs in the balance!")  # Print the chosen category here
                chosen_list = categories[chosen_category]  # chosen_list refers to a list of words associated with the category that the user has chosen to play with.
                return chosen_category, chosen_list
            else:
                print(" ")
                print("I see you're struggling with your keyboard skills.")
                print(" ")
                print (Fore.RED + f"{name}, Please enter a number between 1 and 5." + Style.RESET_ALL)
        else:
            print("Is that character part of a secret code?") 
            print(" ")
            print(Fore.RED + f"{name}, Please enter a number." + Style.RESET_ALL)

def chosen_category_word(chosen_list):
    word = random.choice(chosen_list)
    while '-' in word or ' ' in word:
        word = random.choice(chosen_list) # randomly choose a word fron the chosen category
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
        print (" ")
        print('You have', chosen_level_lives - mistakes, 'lives left.')
        print(Fore.CYAN + "—" * 22 + Style.RESET_ALL)  # Blue decorative line
        print(" ")
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word:', ' '.join(word_list))
        print('Used letters:', ' '.join(used_letters))
        print(" ")
        user_letter = input('Guess a letter: \n').upper()
        if user_letter in alphabet - used_letters:
            clear_terminal()
            used_letters.add(user_letter)
            if user_letter in word_letters:
                print ("The eagle has landed! Or was it a penguin?")
                print(" ")
                print ("No matter, you guessed right!")
                word_letters.remove(user_letter)
            else:
                mistakes += 1
                print("Yikes! Swing and a miss...")
        elif user_letter in used_letters:
            clear_terminal()
            print("Oopsie! That letter's already been served. Let's order something new!")
        else:
            clear_terminal()
            print(" ")
            print("The keyboard gremlins just ate your character!")
            print(" ")
            print(Fore.RED + "Please choose a valid one before they attack again." + Style.RESET_ALL)

    if mistakes == chosen_level_lives:
        display_hangman(mistakes, chosen_level)
        print(" ")
        print("Aw, shucks! Looks like your brain went on vacation with the penguins.") 
        print("The word was", Fore.GREEN + word + Style.RESET_ALL)
        print(" ")
    else:
        print(" ")
        print("The word was", Fore.GREEN + word + Style.RESET_ALL)
        print(" ")
        print("You guessed it! Your detective skills are sharper than Sherlock Holmes on a caffeine bender.")
        print(" ")

def continue_game():
    while True:
        print("Ready for another round? It's like potato chips, you can't have just one. (y/n)")
        choice = input().lower()

        if choice == "y":
            clear_terminal()  # Assuming you have a clear_terminal function defined
            print("Oh good, you haven't given up yet. This could get interesting...")
            print(" ")
            while True:
                you_sure = input("Are you sure? (y/n) ").lower()
                if you_sure in ("y", "n"):  # Check for both "y" and "n"
                    if you_sure == "y":
                        clear_terminal()
                        hangman()  # Assuming you have a hangman function defined
                        break  # Exit inner loop on confirmation
                    elif you_sure == "n":
                        print(" ")
                        print("Farewell, brave soul! Remember, quitting is bravery... sometimes.")
                        print(" ")
                        print("Don't tell my therapist I said that.")
                        print(" ")
                        return  # Exit the function, effectively ending the game
                else:
                    print(Fore.RED + "Please enter 'y' or 'n'." + Style.RESET_ALL)
        elif choice == "n":  # Handle "n" from the first prompt directly
            clear_terminal()
            print(" ")
            print("Thanks for playing!")
            print(Fore.CYAN + "—" * 19 + Style.RESET_ALL)  # Blue decorative line
            print(" ")
            print("...and please excuse any existential dread")
            print("you may have experienced during the game.")
            print(" ")
            print("I'm still under development, after all :-)")
            print(" ")
            break  # Exit the entire loop after farewell message
        else:
            print("Wow, that was... something.")
            print(" ")
            print("Are you trying to speak Morse code?")
            print(" ")
            print(Fore.RED + "Please enter 'y' or 'n'." + Style.RESET_ALL)









if __name__ == "__main__":
    hangman()
    continue_game()
