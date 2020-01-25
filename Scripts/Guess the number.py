# Project 1 - Guess the number

# imports
import random

# setting up a counter that counts the number of plays
guessesTaken = 0

# Inserting the player name
print "Hello!! What's your name?"
playerName = raw_input()

# set the random number var
randNumber = random.randint(1, 20)
print "Well, " + playerName + "I am thinking of a number between 1 and 20"

while guessesTaken < 6:
    print "Take a guess."
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < randNumber:
        print "Your guess is too low"

    if guess > randNumber:
        print "Your guess is too high"

    if guess == randNumber:
        break

if guess == randNumber:
    guessesTaken = str(guessesTaken)
    "Congratulations " + playerName + "!! You've guessed the number in " + guessesTaken + " guesses."


if guesses != randNumber:
    number = str(randNumber)
    print "Nope. " + guess + " is not the number i was thinking of. The correct answer would be " + randNumber
