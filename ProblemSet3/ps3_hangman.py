# -*- coding: utf-8 -*-

# Hangman game
#

# -----------------------------------
# Helper code

import random
import string

WORDLIST_FILENAME = "/Users/hanaum/Documents/6.00.1xFiles/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    letterList = []
    for letter in secretWord:
        if letter in lettersGuessed:
            letterList.append(letter)
        else:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    words = "_" * len(secretWord)
    wordList = list(words)
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            del(wordList[i])
            wordList.insert(i, secretWord[i])
    wordList = " ".join(wordList)
    return wordList

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in alpha:
            alpha = alpha.replace(lettersGuessed[i], "")
    return alpha


def hangman(secretWord):

    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    num_guesses = 8
    lettersGuessed = []
    remainingLetters = getAvailableLetters(lettersGuessed)
    wordList = getGuessedWord(secretWord, lettersGuessed)

    while num_guesses > 0:
        guess = raw_input("Please guess a letter: ")

        if guess in lettersGuessed and lettersGuessed is not None:
            print "Oops! you've already guessed that letter: ", guess

        lettersGuessed.append(guess)
        if guess in secretWord:
            wordList = getGuessedWord(secretWord, lettersGuessed)
            remainingLetters = getAvailableLetters(lettersGuessed)
            print "You have " + str(num_guesses) + " guesses left."
            print "Available letters: ", remainingLetters
            print "Good guess: ", wordList
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print "Congratulations, you won!"
                break
        else:
            num_guesses -= 1
            print "You have " + str(num_guesses) + " guesses left."
            print "Available letters: ", remainingLetters
            print "Oops! That letter is not in my word: ", wordList

    print "Sorry, you ran out of guesses. The word was ", secretWord



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
