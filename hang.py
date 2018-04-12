import random
import string

WORDLIST_FILENAME = "palavras.txt"

def load_secret_words():
    in_file = open(WORDLIST_FILENAME, 'r', 0)
    line = in_file.readline()
    word_list = string.split(line)
    return word_list

def sort_secret_word(word_list):
    random_word = random.choice(word_list)
    random_word_lowercase = random_word.lower()
    return random_word_lowercase

def generate_secret_word():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."

    word_list = load_secret_words()
    word_count = len(word_list)

    print "  ", word_count, "words loaded."

    secret_word = sort_secret_word(word_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter in letters_guessed:
            pass
        else:
            return False

    return True

def get_available_letters():
    import string
    # the next line will return 'abcdefghijklmnopqrstuvwxyz'
    available_letters = string.ascii_lowercase
    return available_letters

def remove_letter(letter, letters):
    return letters.replace(letter, '')

def clean_available_letters(letters_guessed):
    available_letters =  get_available_letters()
    for letter in available_letters:
        if letter in letters_guessed:
            available_letters = remove_letter(letter, available_letters)
    return available_letters

def unique_letters_count(secret_word):
    unique_letters_list = []
    for letter in secret_word:
        if not letter in unique_letters_list:
            unique_letters_list.append(letter)

    unique_letters_count = len(unique_letters_list)
    return unique_letters_count

def build_guessed_word(secret_word, letters_guessed):
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += " _ "
    return guessed_word

def can_change_word(unique_letters, guesses_left):
    return unique_letters > guesses_left

def print_hangman_header(secret_word_length, unique_letters_count):
    print 'I am thinking of a word that is', secret_word_length, ' letters long.'
    print 'The secret word has ', unique_letters_count, ' unique letters.'
    print '-------------'


def read_letter_input(change_word):
    if change_word:
        print 'You are running out of guesses! Insert 0 to change the word.'
    letter = raw_input('Please guess a letter: ')
    return letter

def already_guessed_letter(secret_word, letters_guessed):
    guessed_word = build_guessed_word(secret_word, letters_guessed)
    print 'Oops! You have already guessed that letter: ', guessed_word

def guessed_letter(secret_word, letters_guessed):
    guessed_word = build_guessed_word(secret_word, letters_guessed)
    print 'Good Guess: ', guessed_word

def wrong_guessed_letter(secret_word, letters_guessed):
    guessed_word = build_guessed_word(secret_word, letters_guessed)
    print 'Oops! That letter is not in my word: ',  guessed_word

def ended_hangman(secret_word, letters_guessed):
    if is_word_guessed(secret_word, letters_guessed) == True:
        print 'Congratulations, you won!'

    else:
        print 'Sorry, you ran out of guesses. The word was ', secret_word, '.'
    quit()

def hangman(secret_word):
    guesses_left = 8
    letters_guessed = []
    secret_word_length = len(secret_word)
    unique_letters = unique_letters_count(secret_word)

    print_hangman_header(secret_word_length, unique_letters)

    while is_word_guessed(secret_word, letters_guessed) == False and guesses_left > 0:
        available_letters = clean_available_letters(letters_guessed)
        change_word = can_change_word(unique_letters, guesses_left)

        print 'You have ', guesses_left, 'guesses left.'
        print 'Available letters', available_letters

        letter = read_letter_input(change_word)

        if letter == '0' and change_word:
            start_hangman()

        elif letter in letters_guessed:
            already_guessed_letter(secret_word, letters_guessed)

        elif letter in secret_word:
            letters_guessed.append(letter)
            guessed_letter(secret_word, letters_guessed)

        else:
            guesses_left -= 1
            letters_guessed.append(letter)
            wrong_guessed_letter(secret_word, letters_guessed)

        print '------------'

    else:
        ended_hangman(secret_word, letters_guessed)

def start_hangman():
    secret_word = generate_secret_word()
    hangman(secret_word)

def main():
    print 'Welcome to the game, Hangam!'
    start_hangman()

main()
