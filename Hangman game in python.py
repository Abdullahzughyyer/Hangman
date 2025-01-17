#Abdallah Zughyyer

import random

hangman_graphics = [
          """
           _______
          |       |
          |       O
          |
          |
          |
         _|_
        |   |______
        |__________|
        """,

        """
           _______
          |       |
          |       O
          |       |
          |
          |
         _|_
        |   |______
        |__________|
        """,

        """
           _______
          |       |
          |       O
          |       |/
          |
          |
         _|_
        |   |______
        |__________|
        """,

        """
           _______
          |       |
          |       O
          |      \|/
          |
          |
         _|_
        |   |______
        |__________|
        """,

        """
           _______
          |       |
          |       O
          |      \|/
          |       |
          |
         _|_
        |   |______
        |__________|
        """,


        """
           _______
          |       |
          |       O
          |      \|/
          |       |
          |      /
         _|_
        |   |______
        |__________|
        """,

        """
           _______
          |       |
          |       O
          |      \|/
          |       |  Be careful!!
          |      / \         
         _|_
        |   |______
        |__________|
        """

    
]


def select_word(category):
    if category.lower() == "technology":
        words = ["computer", "internet", "software", "code", "algorithm"]
    elif category.lower() == "education":
        words = ["science", "mathematics", "programing", "history", "arabic"]
    elif category.lower() == "sports":
        words = ["football", "basketball", "tennis", "volleyball", "swimming"]
    elif category.lower() == "cars":
        words = ["mercedes", "bmw", "lexus", "coupe", "hyundai"]
    elif category.lower() == "food":
        words = ["pizza", "burger", "pasta", "sushi", "sandwich"]
    elif category.lower() == "animals":
        words = ["horse", "cat", "mouse", "lion", "tiger"]
    else:
        print("Invalid category!")
        return None

    return random.choice(words)

def display_hangman(incorrect_guesses):
    print(hangman_graphics[incorrect_guesses])

    
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    print(displayed_word)

def is_word_guessed(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def play_hangman():
    print("Welcome to Hangman!")
    player = input("Player , please enter your name: ")

    while True:
        category = input("Please choose a category (Technology, Education, Sports, Cars, Food, Animals): ")
        word = select_word(category)
        if word:
            break

    guessed_letters = []
    incorrect_guesses = 0

    print(f"{player}, you have 7 attempts to guess the word.")
    while incorrect_guesses < 7:
        display_hangman(incorrect_guesses)
        display_word(word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            print("Correct guess!")
            guessed_letters.append(guess)
            if is_word_guessed(word, guessed_letters):
                print(f"Congratulations, {player}! You've guessed the word '{word}' correctly.")
                break
        else:
            print("Incorrect guess!")
            guessed_letters.append(guess)
            incorrect_guesses += 1

    if incorrect_guesses == 7:
        print("Sorry, you've run out of attempts. The word was:", word)
        print("Try again, don't lose hope -_- ")

    
    replay = input("Do you want to play again? (yes/no): ")
    if replay.lower() == "yes":
        play_hangman()
    else:
        print("Thank you for playing Hangman!")


play_hangman()
