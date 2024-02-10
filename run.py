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

levels = {
    "Easy - 8 lives: Perfect for hangman beginners": 8,
    "Hard - 4 lives: For the daring souls who seek a challenge": 4
}

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
    
    print(hangman_stages[stages_to_display])
    return stages_to_display

def choose_level():
    print("Welcome to Hangman Madness!")
    print("---------------------------")
    print("Prepare yourself for an epic journey through the alphabet jungle.")
    print(" ")
    print("Step 1: Choose Your Level of Adventure!")
    print("---------------------------------------")
    for i, level in enumerate(levels):
        print(f"{i+1}. {level}")

    while True:
        print(" ")
        choice = input("Enter your level (1-2): \n")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(levels):
                chosen_level = list(levels.keys())[choice]
                print("You selected:")
                print("-------------")
                print(chosen_level + ".",)  # Print the chosen category here
                print(" ")
                print("Excellent choice!")
                print(" ")
                chosen_level_lives = levels[chosen_level]  # chosen_list refers to a list of words associated with the category that the user has chosen to play with.
                return chosen_level, chosen_level_lives
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        else:
            print("Invalid choice. Please enter a number.")

def choose_category():
    print("Step 2: Let's explore the world of letters! Choose your favorite category!")
    print("---------------------------------------------------------------------------")
    for i, category in enumerate(categories):
        print(f"{i+1}. {category}")

    while True:
        print (" ")
        choice = input("Enter your choice (1-5): \n")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(categories):
                chosen_category = list(categories.keys())[choice]
                print("You selected", chosen_category + ".",)
                print(" ")
                print("Step 3: Let the guessing games begin!")
                print("-------------------------------------")
                print("On your marks, get set, guess! The hangman's rope hangs in the balance!")  # Print the chosen category here
                chosen_list = categories[chosen_category]  # chosen_list refers to a list of words associated with the category that the user has chosen to play with.
                return chosen_category, chosen_list
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        else:
            print("Invalid choice. Please enter a number.")

def chosen_category_word(chosen_list):
    word = random.choice(chosen_list)
    while '-' in word or ' ' in word:
        word = random.choice(chosen_list) # randomly choose a word fron the chosen category
    return word.upper()

def hangman():
    chosen_level, chosen_level_lives = choose_level()
    chosen_category, chosen_list = choose_category()
    word = chosen_category_word(chosen_list)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    mistakes = 0

    while len(word_letters) > 0 and mistakes < chosen_level_lives:
        display_hangman(mistakes, chosen_level)
        print (" ")
        print('You have', chosen_level_lives - mistakes, 'lives left.')
        print("----------------------")
        print(" ")
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word:', ' '.join(word_list))
        print('Used letters:', ' '.join(used_letters))
        print(" ")
        user_letter = input('Guess a letter: \n').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                print ("The eagle has landed! (Or was it a penguin? No matter, you guessed right!)")
                word_letters.remove(user_letter)
            else:
                mistakes += 1
                print("Yikes! Swing and a miss...")
        elif user_letter in used_letters:
            print("Oopsie! That letter's already been served. Let's order something new!")
        else:
            print(" ")
            print("The keyboard gremlins just ate your character! Please choose a valid one before they attack again.")

    if mistakes == chosen_level_lives:
        display_hangman(mistakes, chosen_level)
        print(" ")
        print("Aw, shucks! Looks like your brain went on vacation with the penguins. The word was", word)
    else:
        print(" ")
        print("You guessed it! Your detective skills are sharper than Sherlock Holmes on a caffeine bender.")

def continue_game():
    while True:
        print()
        continue_playing = input("Ready for round two? It's like potato chips, you can't have just one. (y/n) \n")
        if continue_playing.lower() == "y":
            print("Oh good, you haven't given up yet. This could get interesting...")
            hangman()
        elif continue_playing.lower() == "n":
            print("Farewell, brave soul! Remember, quitting is bravery... sometimes. Don't tell my therapist I said that.")
            break
        else:
            print("Wow, that was... something. Are you trying to speak Morse code? Please try again.")

    print("Phew, that was almost too close for comfort! Thanks for playing, and please excuse any existential dread you may have experienced during the game. I'm still under development, after all.")
    print(" ")

hangman()
continue_game()
