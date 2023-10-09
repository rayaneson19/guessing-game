#guessing game
#test

import random

correct_guess = False
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
s_n = random.choice(list1)
guess = 1 
guess_limit= 5
v = input("   \n     Hello, Tell me you name:    ")


try:
        w= print('   \nHi '+ v + '. Lets play a game!. Im thinking of a number between 1 to 15. You think you are able to guess it?, just so you know you have 5 tries.')
        while guess <= guess_limit:
                if guess <= 1:
                        w = int(input('    \n Take a guess:    '))
                else:
                
                        w = int(input('    \n Take another guess:    '))

                if w == s_n:
                        correct_guess = True
                        break
                elif s_n + 1<= w <=s_n +4 and  0 < w <= 15 and guess != 5:
                        print('   \nYour guess was a little bit too high, try again:   ')
                elif s_n - 5 <= w <= s_n - 1 and guess != 5 and 0 < w <= 15:
                        print("   \nYour guess was a little bit too low, try again:   ")
                elif w <= s_n - 6 and guess != 5 and 0 < w <= 15:
                        print("   \nYour guess was way too low, try again:   ")
                elif s_n + 4 <= w and guess != 5 and 0 < w <= 15:
                        print('   \nYour guess was way too high, try guessing lower:   ')
                        
                
                guess += 1
                if guess > guess_limit:
                                print("\nSorry, " + v + ", you've run out of guesses. My number was " + str(s_n) + ".")
                                break

                if w > 15 or w < 1:
                        print("   \nYou can only type numbers between 1 and 15!.")
                        continue
                if correct_guess:
                        print("   \nExcellent job " + v + ", You guessed right!.   ")
                        if guess == 1:
                                print("   \n  You guessed my number in " + str(guess) + " try!.")
                        else:
                                print("   \n  You guessed my number in " + str(guess) + " tries!.")
except ValueError:
    print('   \nYou can only type a number!')