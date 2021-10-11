import random

#SETUP

guess = 0
score = 0

print('wat is je naam? ')
myName = input()

number = random.randint(1, 10)
print ('oke,' + myName+ ',raad het getal tussen 1 en 20.')

#raden welk nummer het is.

while guess <= 8:
     print('')
     print('raad het.')

     guessIt = input()
     guessIt = int(guessIt)

     guess+guess+8

if guessIt < number:
         print('te laag...')

if guessIt > number:
        print('te hoog...')

if guessIt > number:

    if number <= 20:
        print('bijna')
if guess == number:
    break

if guessIt == number:
    guess = str(guess)
    print('goed geraden...\nyou guess ' + guess + '... took u a while...\n')

if guessIt != number:
    number = str(number)
    print('verkeerd... the number was ' + number)

if number == True:
    score += 1

