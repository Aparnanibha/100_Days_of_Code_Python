import random
from Hangman_word import word_list

chosen_word = random.choice(word_list)

# Testing the code only
#print(f"The solution is {chosen_word}")

# Creating the blank space
display = []
for _ in chosen_word:
    display += "_"
print(display)

live = 6
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Checking the guess letter
    for position in range(0, len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    # If user repeat the previous guessed letter
    if guess in display:
        print(f"You have already guessed {guess}")
    # If user guessed the wrong letter
    elif guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You loose a life.")
        live -= 1
        if live == 0:
            end_of_game = True
            print("You Loose!!!")

    print(display)
    print(live)

    # Join all the word in the list and turned into string
    print(f"{' '.join(display)}")

    # Check if user got all the letter or not
    if "_" not in display:
        end_of_game = True
        print("You win")

