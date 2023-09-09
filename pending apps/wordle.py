import random


def wordle():
    words = ["apple", "banana", "cherry", "dough", "fudge",
             "grape", "hazel", "jelly", "kitty", "lemon",
             "mango", "olive", "peach", "quail", "razor",
             "snake", "tiger", "umbra", "viper", "wrist",
             "zebra", "beach", "clamp", "drape", "flint",
             "globe", "hatch", "icicle", "jigsaw", "kale",
             "lucky", "mirth", "nudge", "opera", "plum",
             "quack", "rival", "silly", "tramp", "ultra",
             "vivid", "waste", "xerox", "yacht", "zeal",
             "abide", "blaze", "chaos", "drown", "evoke",
             "flora", "grind", "hymns", "image", "jumps",
             "keeps", "lunar", "mints", "noble", "ozone",
             "pride", "quake", "relic", "saint", "taste",
             "upend", "vague", "wound", "xenon", "yield",
             "zilch", "ambit", "bloom", "cloak", "dwell",
             "enact", "frisk", "grasp", "haste", "input",
             "joker", "knack", "liver", "march", "noble",
             "opium", "proud", "quake", "rider", "swoop",
             "taste", "under", "vault", "whale", "xenon",
             "yield", "zesty", "juicy", "kneel", "zesty",
             "barge", "cider", "drift", "elbow", "fable",
             "giant", "horse", "irons", "juice", "kings",
             "latch", "merry", "naval", "oasis", "pouch",
             "quiet", "rhino", "sneak", "truce", "utter",
             "vowel", "waxen", "youth", "zebra", "abide",
             "bliss", "coral", "deity", "elope", "flute",
             "glint", "haste", "ivory", "jokes", "knack",
             "leash", "mirth", "night", "ocean", "pride",
             "quilt", "rival", "sailor", "tramp", "unzip",
             "vivid", "wager", "xylo", "yearn", "zesty",
             "arise", "brave", "cloud", "daisy", "eagle",
             "flask", "grain", "heist", "input", "jolly",
             "kiosk", "lunar", "mould", "novel", "ozone",
             "prism", "quiet", "rider", "shade", "trick",
             "uncle", "vivid", "wrist", "xenon", "yacht",
             "zebra", "abide", "blink", "crane", "dwell",
             "elbow", "flame", "grape", "hoist", "islet",
             "jumps", "keen", "laser", "maize", "noble",
             "oasis", "plume", "quail", "rover", "steer",
             "tiger", "umbra", "viper", "whale", "xerox",
             "youth", "zeal", "adore", "blitz", "cubic",
             "drown", "elate", "flora", "gnome", "haste",
             "inert", "juicy", "kneel", "lucid", "moral",
             "nymph", "ounce", "prime", "quilt", "robin",
             "saint", "tramp", "unity", "vague", "waste",
             "xylon", "yearn", "zilch", "amber", "bloom",
             "crisp", "drape", "erase", "flute", "glare",
             "hymns", "inlay", "jokes", "knack", "leash",
             "mirth", "nudge", "ocean", "plumb", "quest",
             "rival", "swoop", "tease", "unity", "vivid",
             "wager", "xylo", "zesty", "abode", "blink",
             "crave", "dwell", "elude", "flora", "grasp",
             "heath", "ivory", "juice", "kiosk", "lunar",
             "mound", "nurse", "oasis", "plume", "quail",
             "rover", "saint", "tramp", "uncle", "vague",
             "waste", "xylon", "yearn", "zilch", "amber",
             "bloom", "crisp", "drape", "erase", "flute",
             "glare", "hymns", "inlay", "jokes", "knack",
             "leash", "mirth", "nudge", "ocean", "plumb",
             "quest", "rival", "swoop", "tease", "unity",
             "vivid", "wager", "xylo", "zesty", "acrid",
             "bland", "champ", "draft", "elope", "flask",
             "glare", "hefty", "ionic", "jolly", "kiosk",
             "latch", "maize", "noble", "ocean", "plume",
             "quilt", "rover", "saint", "tramp", "uncle",
             "vivid", "wrist", "xenon", "yacht", "zebra",
             "abide", "blink", "crane", "dwell", "elbow",
             "flame", "grape", "hoist", "islet", "jumps",
             "keen", "laser", "maize", "noble", "oasis",
             "plume", "quail", "rover", "steer", "tiger",
             "umbra", "viper", "whale", "xerox", "youth",
             "zeal", "adore", "blitz", "cubic", "drown",
             "elate", "flora", "gnome", "haste", "inert",
             "lucid", "moral", "nymph", "ounce", "prime",
             "quilt", "robin", "saint", "tramp", "unity",
             "vague", "waste", "xylon", "yearn", "zilch",
             "amber", "bloom", "crisp", "drape", "erase",
             "flute", "glare", "hymns", "inlay", "jokes",
             "knack", "leash", "mirth", "nudge", "ocean",
             "plumb", "quest", "rival", "swoop", "tease",
             "unity", "vivid", "wager", "xylo", "zesty",
             "abode", "blink", "crave", "dwell", "elude",
             "flora", "grasp", "heath", "ivory", "juice",
             "kiosk", "lunar", "mound", "nurse", "oasis",
             "plume", "quail", "rover", "saint", "tramp",
             "uncle", "vague", "waste", "xylon", "yearn",
             "zilch", "amber", "bloom", "crisp", "drape",
             "erase", "flute", "glare", "hymns", "inlay",
             "jokes", "knack", "leash", "mirth", "nudge",
             "ocean", "plumb", "quest", "rival", "swoop",
             "tease", "unity", "vivid", "wager", "xylo",
             "zesty", "acrid", "bland", "champ", "draft",
             "elope", "flask", "glare", "hefty", "ionic",
             "jolly", "kiosk", "latch", "maize", "noble",
             "ocean", "plume", "quilt", "rover", "saint",
             "tramp", "uncle", "vivid", "wrist", "xenon",
             "yacht", "zebra", "abide", "blink", "crane",
             "dwell", "elbow", "flame", "grape", "hoist",
             "islet", "jumps", "keen", "laser", "maize",
             "noble", "oasis", "plume", "quail", "rover",
             "steer", "tiger", "umbra", "viper", "whale",
             "xerox", "youth", "zeal", "adore", "blitz",
             "cubic", "drown", "elate", "flora", "gnome",
             "haste", "inert", "juicy", "kneel", "lucid",
             "moral", "nymph", "ounce", "prime", "quilt",
             "robin", "saint", "tramp", "unity", "vague",
             "waste", "xylon", "yearn", "zilch", "amber",
             "bloom", "crisp", "drape", "erase", "flute",
             "glare", "hymns", "inlay", "jokes", "knack",
             "leash", "mirth", "nudge", "ocean", "plumb",
             "quest", "rival", "swoop", "tease", "unity",
             "vivid", "wager", "xylo"]
    hidden_word = random.choice(words)
    attempts = 6
    guessed_word = "_____"
    print("Welcome to wordle!")
    print(f"You have {attempts} attempts to guess the five-letter word.")
    print(guessed_word)

    while attempts > 0:
        guess = input("Enter you guess: ").lower()
        if guess == "/give up":
            print(f"The word was {hidden_word}")
            break
        if guess == "/help":
            print("\nHow to Play\n"
                  "-----------\n"
                  "- In each game, you have 6 attempts to guess a random word\n"
                  "- When the word contains a letter in your guess but is in the wrong place, the feedback will show "
                  "'O'\n"
                  "- When the word contains a letter in your guess and is in the correct place, the feedback will "
                  "show'X'\n"
                  "- Other letters will be shown as '_'\n"
                  "- To give up, type /give up\n"
                  "- To exit, type /exit")
            continue
        if guess == "/exit":
            print("Exited")
            break
        if len(guess) != 5:
            print("Please enter a five-letter word.")
            continue
        if guess == hidden_word:
            print(f"Congratulations! You've guessed the word: {hidden_word}")
            break
        feedback = ""
        for i in range(5):
            if guess[i] == hidden_word[i]:
                feedback += "X"
            elif guess[i] in hidden_word:
                feedback += "O"
            else:
                feedback += "_"
        print(feedback)
        attempts -= 1
        print(f"Attempts remainding: {attempts}")
        if attempts > 0:
            print(guessed_word)
    if attempts == 0:
        print(f"Sorry, you've run out of attempts.The word was {hidden_word}")


wordle()
