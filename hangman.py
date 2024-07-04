import random

def choose_word():
    words = ["apple", "banana", "orange", "strawberry", "grape", "blueberry", "pineapple", "apricot", "peach", "mango"]
    return random.choice(words)

def hangman():
    max_attempts = 6
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    incorrect_letters = set()
    
    while len(incorrect_letters) < max_attempts:
        display_word = ''.join(letter if letter in guessed_letters else '_' for letter in word)
        print(f"Word: {display_word}")
        
        if guessed_letters:
            print(f"Guessed letters: {' '.join(guessed_letters)}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters or guess in incorrect_letters:
            print("You already guessed that letter.")
        elif guess.isalpha() and len(guess) == 1:
            guessed_letters.add(guess)
            if guess in word_letters:
                print("Correct!")
                if all(letter in guessed_letters for letter in word_letters):
                    print(f"Congratulations! You guessed the word '{word}' correctly!")
                    return
            else:
                print("Incorrect guess.")
                incorrect_letters.add(guess)
        else:
            print("Invalid input. Please enter a single letter.")
        
        print(f"Attempts left: {max_attempts - len(incorrect_letters)}")
        print_hangman(len(incorrect_letters))
        print()
    print(f"Oops! You ran out of attempts. The word was '{word}'.")

def print_hangman(num_wrong):
    stages = [  # final state: head, torso, both arms, and both legs
        # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                 _/|\\_
                """,

        # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                 _/|\\_
                """,

        # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                 _/|\\_
                """,

        # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                 _/|\\_
                """,

        # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                 _/|\\_
                """,

        # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                 _/|\\_
                """, 

        # final state
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                 _/|\\_
                """
                         
    ]
    print(stages[num_wrong])

# Start the game
hangman()
