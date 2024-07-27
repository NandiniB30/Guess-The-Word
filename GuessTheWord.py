import random

words = ["apple", "banana", "mango", "strawberry", "orange", "grape", "pineapple", "apricot", "lemon", "coconut",
         "watermelon", "cherry", "papaya", "berry", "peach", "lychee", "muskmelon"]

# randomly choose a word from words
word = random.choice(words)
guesses = ''
# any number of turns = total character in words +2
turns = len(word) + 2
print("Guess the word! HINT: word is a name of a fruit.")

while turns >= 0:
    # flag to count the number of character correctly guessed
    correct = 0
    # all characters from chosen taken one at a time.
    for char in word:
        # comparing each character with the character in str guesses
        # if character from chosen word exists in guesses then print it else print '_' in its place
        if char in guesses:
            print(char, end=" ")
            correct += 1
        else:
            print("_", end=" ")
    print()
    if correct == len(word):
        # user will win the game they correctly guess all the character of word
        print("Congratulations, You won!")
        # this print the correct word
        print("The word is:", word)
        break
    elif turns == 0:
        print("No more guesses.You lost! Try again..")
        break
    elif turns == 1:
        print("Last guess!!")

    # fetch user's guess of character
    print()
    print("You've got {turns} guesses.")
    guess = input("Guess a character of word:")

    # Validation of the guess
    if not guess.isalpha():
        print('Enter only a LETTER')
        continue
    elif len(guess) > 1:
        print('Enter only a SINGLE letter')
        continue
    elif guess in guesses:
        print('You have already guessed that letter')
        continue

    # every guessed character from user will be stored in guesses
    guesses += guess

    turns -= 1
    # check guessed character with the character in word
    if guess not in word:
        # if the character does’t match the word
        # then “Letter not present in word.Try Again!” will be given as output
        print("Letter not present in word.Try Again!")



