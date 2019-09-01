#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')#code says greetings
colors = ['red','orange','yellow','green','blue','violet','purple']#makes a list of colors
play_again = ''#assigns play_again to a blank space
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'):#loops as long as play_again isn't assigned to n or no
    match_color = random.choice(colors)#assigns match_color randomly to a color in the list color
    count = 0#sets count to 0
    color = ''#sets color to blank space
    while (color != match_color):#loops until color=match_color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line,asks question and lets you guess
        color = color.lower().strip()#removes spaces and makes it lowercase
        count += 1#count increases by 1
        if (color == match_color):#checks if color=match_color
            print('Correct!')#prints correct
        else:#goes if if isn't met
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))#tells you your wrong and amount of times you guessed
    print('\nYou guessed it in {0} tries!'.format(count))#when done tells you how many tries it took
    if (count < best_count):#checks if you did better than your best
        print('This was your best guess so far!')#prints the msg
        best_count = count#best_count is assigned to your new best
    play_again = input("\nWould you like to play again? ").lower().strip()#asks if you want to play again and lets you answer
print('Thanks for playing!')#prints the msg