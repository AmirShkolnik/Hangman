# List with 100 animals

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

# List with 50 countries

countries = [
        "Brazil", "Japan", "France", "Italy", "Germany", "Canada", "Australia", "Mexico", "India", "China",
        "Spain", "Russia", "Argentina", "SouthAfrica", "SouthKorea", "Netherlands", "Switzerland", "Sweden",
        "Portugal", "Belgium", "Norway", "Denmark", "Finland", "Greece", "Egypt", "Turkey", "Thailand", "Iran",
        "Vietnam", "Poland", "Ukraine", "Indonesia", "Philippines", "Malaysia", "Israel", "SaudiArabia",
        "Pakistan", "Bangladesh", "Nigeria", "Kenya", "Morocco", "Peru", "Chile", "Colombia", "Venezuela",
        "Cuba", "NewZealand", "Ireland", "Austria", "Hungary"

]

# List with 50 flowers

flowers = [
    "rose", "tulip", "daisy", "lily", "sunflower", "orchid", "daffodil", "peonies", "hydrangea", "carnation",
    "poppy", "marigold", "lavender", "chrysanthemum", "hibiscus", "gerbera", "snapdragon", "freesia", "iris",
    "aster", "zinnia", "dahlia", "crocus", "azalea", "anemone", "cosmos", "lilac", "hyacinth", "geranium",
    "pansy", "forgetmenot", "bougainvillea", "camellia", "ranunculus", "gladiolus", "fuchsia", "birdofparadise",
    "buttercup", "columbine", "delphinium", "foxglove", "gardenia", "larkspur", "narcissus", "peony",
    "sweetpea", "tigerlily", "verbena", "wisteria"
    
]

# List with 50 languages

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

# List with 50 fruits

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

import random
import string

categories = {
    "Animals": animals,
    "Countries": countries,
    "Flowers": flowers,
    "Languages": languages,
    "Fruits": fruits
}

def choose_category():
    print("Choose a category to play with:")
    for i, category in enumerate(categories):
        print(f"{i+1}. {category}")

    choice = int(input("Enter your choice (1-5): \n")) - 1

    if choice < 0 or choice >= len(categories):
        print("Invalid choice. Please try again.")
        return choose_category()  # Recursive call to prompt the user again
    else:
        chosen_category = list(categories.keys())[choice]
        chosen_list = categories[chosen_category]
        return chosen_category, chosen_list

def get_valid_word(words_list):
    word = random.choice(words_list)
    while '-' in word or ' ' in word:
        word = random.choice(words_list)
    return word.upper()


def get_valid_word(words_list):
    word = random.choice(fruits)  # randomly choose a fruit from the fruits list
    while '-' in word or ' ' in word:
        word = random.choice(fruits)
    return word.upper()

def display_hangman(mistakes):
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
    
    print(hangman_stages[mistakes])

def hangman():
    word = get_valid_word(fruits)
    word_letters = set(word)    # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    # what the user has guessed

    mistakes = 0
    # getting user input
    while len(word_letters) > 0 and mistakes < 7:
        # display hangman
        display_hangman(mistakes)

        # letters used
        # ' '.join(['a', 'b',  'cd']) --> 'a b cd'
        print('You have', 7 - mistakes, 'lives left and you have used these letters:', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        user_letter = input('Guess a letter: \n').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                mistakes += 1  # increment mistake count if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0 OR when mistakes == 7
    if mistakes == 7:
        display_hangman(mistakes)
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')

def continue_game():
    play_game = True
    while play_game:
        continue_playing = input("Would you like to continue playing the game? y/n \n")
        
        if continue_playing.lower() == "y":
            print("You have decided to continue playing the game.")
            hangman() # restart the game if user chooses to continue
        elif continue_playing.lower() == "n":
            print("Now closing the game...")
            play_game = False
        else:
            print("That is not a valid option. Please try again.")

    print("Thanks for playing")

choose_category()
hangman()
continue_game()