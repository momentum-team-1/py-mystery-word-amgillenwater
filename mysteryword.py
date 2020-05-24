import random

# random word function, exclude words that start with uppercase
def get_random_word(list):
    """ this function returns a random word from the word list given """
    random_word = random.choice(list)
    random_lower_word = random_word.lower()
    print (random_lower_word)
    return random_lower_word

def what_level(word_list):
    """This function will sort the word list by length for each level chosen--ran before the user input function for their guesses. 
    Maybe this function needs to happen before the random function, too? narrow down the list to the lengths selected, then randomly pick a word?
    """
    desired_level = input("Please type one of the following to indicate the level of difficulty you'd like to play: Easy, Normal, Difficult  ")
    new_word_list = []
    if desired_level.lower() == 'easy':
        for word in word_list:
            if len(word) >= 4 and len(word) <= 6:
                new_word_list.append(word)
                
                #need to figure out how to send this list to the random function, return it?
    if desired_level.lower() == 'normal':
        for word in word_list:
            if len(word) >= 6 and len(word) <= 8:
                new_word_list.append(word)
              
    if desired_level.lower() == 'hard':
        for word in word_list:
            if len(word) <= 8:
                new_word_list.append(word)

    print(new_word_list)
#userinput function
def user_input():
    user_input = input("Please guess a letter:  ")
    lower_letter = user_input.lower()
    print (lower_letter)


def main(file):
    opened_file = open(file)
    word_list = opened_file.read().split()
    what_level(word_list)
    # get_random_word()
    user_input()

main('words.txt')

# if __name__ == "__main__":
#     main()


# ask user what level they would like to play
    #level conditions for random word selection?
# random word function
# game starts by showing user how many characters are in the random word chosen
# game alerts user that they have 8 guesses left
    #guess tracker/counter
#game asks user to make a guess and provides an input prompt
    #input function
#user inputs a letter
    #we take the input and compare it to the random word's letters
    #add the input to the string of guessed letters
#game shows empty spaces of word and if the letter is correct, it fills the letter in the correct spot
    #vanna white function
        #needs to have the random word and the string of guessed letters
        #returns a string of letters that the user has guessed and underscores to represent letters in the mystery word that they have not guessed yet.
#game prompts user to continue guessing until the guess counter = 0
# if user guesses wrong, they lose a guess
    #if input != letter in the word, counter -= 1
    #if user guesses correctly, counter stays the same
# if user makes a duplicate guess, game alerts user they have already guessed that letterr
    #if input is already in the string that keeps track of guesses, print the error msg

