from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def isWord(word, hand, wordList):

    new_hand = hand.copy()
    for letter in word:
        if letter not in hand:
            return False
        elif letter in hand:
            new_hand[letter] -= 1
            if new_hand[letter] < 0:
                return False
    if word in wordList:
        return True
    else:
        return False

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    best_score = 0
    best_word = None

    for word in wordList:
        if  isWord(word, hand, wordList) == True:
            score = getWordScore(word, n)
            if score > best_score:
                best_score = score
                best_word = word
    return best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total_score = 0
    current_hand = hand

    while n > 0:
        print "Current Hand: ",
        displayHand(current_hand)
        word = compChooseWord(current_hand, wordList, n)
        if word == None:
            break
        total_score += getWordScore(word, n)
        print "'" + word + "'" + " earned " + str(getWordScore(word , n)) + " points. " + "Total: " + str(total_score) + " points\n"
        current_hand = updateHand(current_hand, word)
        if calculateHandlen(current_hand) == 0:
            break

    if calculateHandlen(current_hand) == 0:
        print "Total score: " + str(total_score) + " points."
    else:
        print "Total Score: " + str(total_score) + " points."

#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    previous_hand = {}
    start = True
    n = HAND_SIZE

    while start:
        option = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if option == 'e':
            start = False
        elif option == 'n':
            hand = dealHand(n)
            while True:
                player = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if player == 'u':
                    playHand(hand, wordList, n)
                    previous_hand = hand
                    break
                elif player == 'c':
                    compPlayHand(hand, wordList, n)
                    previous_hand = hand
                    break
                else:
                    print "Invalid command."
        elif option == 'r':
            if previous_hand == {}:
                print "You have not played a hand yet. Please play a new hand first!"
            else:
                while True:
                    player = raw_input("Enter u to have yourself play, c to have the computer play: ")
                    if player == 'u':
                        playHand(previous_hand, wordList, n)
                        break
                    elif player == 'c':
                        compPlayHand(previous_hand, wordList, n)
                        break
                    else:
                        print "Invalid command."
        else:
            print "Invalid command."


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
