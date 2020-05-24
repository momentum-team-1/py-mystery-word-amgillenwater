import random

# random word function, exclude words that start with uppercase
def get_random_word(list):
    """ this function returns a random word from the word list given, ran after the level choice function"""
    random_word = random.choice(list)
    random_lower_word = random_word.lower()
    print (random_lower_word)
    return random_lower_word

def level_choice(word_list):
    """This function will take user's selection of difficulty and make a new word list that has only words belonging to that difficulty level--this return is then run through the random word choice function
    """
    desired_level = input("Please type one of the following to indicate the level of difficulty you'd like to play: Easy, Normal, Difficult  ")
    new_word_list = []
    if desired_level.lower() == 'easy':
        for word in word_list:
            if len(word) >= 4 and len(word) <= 6:
                new_word_list.append(word)
    if desired_level.lower() == 'normal':
        for word in word_list:
            if len(word) >= 6 and len(word) <= 8:
                new_word_list.append(word)
              
    if desired_level.lower() == 'difficult':
        for word in word_list:
            if len(word) <= 8:
                new_word_list.append(word)
    return new_word_list

def user_input():
    """This function asks for the user's guess and then makes it a lowercase letter for more easy evaluation"""
    user_input = input("Please guess a letter:  ")
    lower_letter = user_input.lower()
    print (lower_letter)


def main(file):
    """This function is where all the other functions will be executed"""
    opened_file = open(file)
    word_list = opened_file.read().split()
    level_selection = level_choice(word_list)
    get_random_word(level_selection)
    user_input()

main('words.txt')

# if __name__ == "__main__":
#     main()


# ask user what level they would like to play
    #level conditions for random word selection?
    #finished!
# random word function
    #finished! 
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

