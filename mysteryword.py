import random

def main(file):
    opened_file = open(file)
    word_list = opened_file.read().split()
    get_random_word(word_list)
    

# random word function, exclude words that start with uppercase
def get_random_word(list):
    """ this function returns a random word from the word list given """
    random_word = random.choice(list)
    random_lower_word = random_word.lower()
    print (random_lower_word)


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
#game shows empty spaces of word and if the letter is correct, it fills the letter in the correct spot
    #vanna white function
#game prompts user to continue guessing until the guess counter = 0
# if user guesses wrong, they lose a guess
    #if input != letter in the word, counter -= 1
    #if user guesses correctly, counter stays the same
# if user makes a duplicate guess, game alerts user they have already guessed that letterr
    #if input is already in the string that keeps track of guesses, print the error msg
