import random
import string

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

def choose_category():
    print("Choose a category to play with:")
    for i, category in enumerate(categories):
        print(f"{i+1}. {category}")

    while True:
        choice = input("Enter your choice (1-5): \n")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(categories):
                chosen_category = list(categories.keys())[choice]
                print("You chose", chosen_category + ".", "Great choice!")  # Print the chosen category here
                chosen_list = categories[chosen_category]  # chosen_list refers to a list of words associated with the category that the user has chosen to play with.
                return chosen_category, chosen_list
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        else:
            print("Invalid choice. Please enter a number.")

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

def chosen_category_word(chosen_list):
    word = random.choice(chosen_list)
    while '-' in word or ' ' in word:
        word = random.choice(chosen_list) # randomly choose a word fron the chosen category
    return word.upper()

def hangman():
    chosen_category, chosen_list = choose_category()
    word = chosen_category_word(chosen_list)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    mistakes = 0

    while len(word_letters) > 0 and mistakes < 8:
        display_hangman(mistakes)
        print('You have', 8 - mistakes, 'lives left.')
        print()
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))
        print('Used letters:', ' '.join(used_letters))
        print()
        user_letter = input('Guess a letter: \n').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                mistakes += 1
                print('Letter is not in word.')
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')

    if mistakes == 8:
        display_hangman(mistakes)
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')

def continue_game():
    while True:
        continue_playing = input("Would you like to continue playing the game? (y/n): \n")
        if continue_playing.lower() == "y":
            print("You have decided to continue playing the game.")
            hangman()
        elif continue_playing.lower() == "n":
            print("Now closing the game...")
            break
        else:
            print("That is not a valid option. Please try again.")

    print("Thanks for playing")


hangman()
continue_game()
