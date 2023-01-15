import random

print("Welcome to hangman \n")


# List of random words
possible_words = ['dog', 'cat', 'pig', 'egg'] # Cannot contain more than 5 letters
word_position = random.randrange(len(possible_words))
the_word = possible_words[word_position]
word_as_list = []
for letters in the_word:
    word_as_list.append(letters)

# Turn word into _
hidden_word = []
for letters in the_word:
    hidden_word.append(letters)
position_of_hidden_letter = 0
for chars in hidden_word:
    hidden_word[position_of_hidden_letter] = "_"
    position_of_hidden_letter += 1


# Post hanging the hangman
print("----|\n|\n|\n|\n----")


# Parts of the hangman
head = "O"
torso = "|"
left_arm = "/"
right_arm = "\\" # Requires two backslashes for no error
left_leg = "/"
right_leg = "\\" # Requires two backslashes for no error


# Game begins here
print(f"Here are the amount of words given: \n{hidden_word} \nStart guessing letters! ")
print(the_word)
the_guess = input("Enter your first letter guess ").lower

if the_guess in the_word:
    print("WOOHOO")
else:
    print("Nope!")