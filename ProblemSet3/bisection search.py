n = int((raw_input("Please enter a number between 0 and 1001: ")))
high = 1000
low = 1
guess = (high+low) / 2

while True:
    print "Is your number " + str(guess) + '?'
    answer = raw_input("Enter 'h' to indiciate the guess is too high. Enter 'l' to indiciate the guess is too low. Enter 'c' to indicate I guessed correctly: ")

    if answer == 'h':
        high = guess
        guess = (high+low) / 2

    elif answer == 'l':
        low = guess
        guess = (high+low) / 2

    elif answer == 'c':
        break

print "So your secret number was: " + str(guess)
