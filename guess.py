#random number
import random

print ('hello can you guess the random number')

random_number= random.randint(1,10000)

guess=None #the users guess
attempts=0 #hoeveel keer geraden is
guessed=False #foute antwoord

while(not guessed):
    guess=int(input("please enter a guess between 1 and 1000"))

    if guess > random_number:
        print ("guess is too high.")
    elif guess < random_number:
        print ("guess is too low.")
    else:
        guessed = True

    attempts += 1

    #the while loop stop

    print  ('you guessed it!\nit took you',attempts,"to guess",random_number)
    print (guess)

