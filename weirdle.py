#!/usr/bin/env python
# coding: utf-8


#wierdle is wordle but partly OOP during classtime <insert date>
#Later, I added 
    #guessed/unguessed letter display
    #input validation checks
    #colors
    #Number the guesses

#todo
    #try / error for importing colorama
        #display different if can't import?
        #MVP = set a flag, then if FLAG==mono print("normally")

    #colorblind mode
    #hard mode (any correct guesses must be included later)

    #executable it to run w less typing eg no  "python3"
    #make annotated Jupyter notebook for educational purposes

    
import colorama
from colorama import Fore, Back, Style
colorama.init()    
    
import string
import random


#should I define my class Game before or after these initial steps?

alphabet = string.ascii_uppercase


#Create the list of valid words 
wordlist = open("wordlist.txt", "r")
wordlist = wordlist.readlines()
wordlist = [w.strip() for w in wordlist]



class Game:
    def __init__(self, word=None):
        if word:
            self.word = word.upper()
        else:
            # TODO: Pick random word from list
            pass
        
        self.guesses = []
        self.letters = []
        

    def is_game_over(self):
        # If number of guesses >= 6 -> over
        if len(self.guesses) >= 6 and self.guesses[-1][0] != self.word:
            self.win = False
            return True
        # If last guess == word -> over
        elif self.guesses and self.guesses[-1][0] == self.word:
            self.win = True
            return True
        else:
            return False
    
    def make_guess(self):

        guess = []

        #todo clarify the validation loop w/ e.g. "while isgood=False"
        #if guess is invalid, keep trying again
        while True:

            print('-' * 40)

#            print("Guess #" + str(len(self.guesses)+1))
#            guess = input("Guess a 5-letter word: ").upper().strip()
            guess = input("Guess #" + str(len(self.guesses)+1) + ": ").upper().strip()

            # New guess must not be empty
            if not guess:
                game.print_board()
                continue

            # New guess must not be wrong length
            elif len(guess) != 5:
                print(Fore.RED + ">>>>>>>Word must be 5 letters long." + Style.RESET_ALL)
                game.print_board()
                continue

            # Check whether guess is one of the allowed words
            elif guess not in wordlist:
                print(Fore.RED + ">>>>>>>Word was not in the word list." + Style.RESET_ALL)
                game.print_board()      
                continue 

            # Check if guess is already guessed before
            elif guess in [item[0] for item in self.guesses]:
                print(Fore.RED + ">>>>>>>Word was already guessed." + Style.RESET_ALL)
                game.print_board()  
                continue 

            #guess is valid, so proceed
            else: 
                break



        #Check if any letters are in the right place

        # TODO: maybe Create actual color_codes for display?
        correct_letter = "G"
        partial_letter = "Y"
        incorrect_letter = "X"

        color_codes = []
        
        true_word_copy = list(self.word)
        
        # First pass: Mark greens
        for i, guess_char in enumerate(guess):
            if guess_char == true_word_copy[i]:
                color_codes.append(correct_letter)
                true_word_copy[i] = '_'
            else:
                color_codes.append('_')
        
        # Second pass: Mark yellows and greys
        for i, guess_char in enumerate(guess):
                
            # Grey if char not in word at all
            if guess_char not in true_word_copy and color_codes[i] != correct_letter:
                color_codes[i] = incorrect_letter
                
            # Naive: In word, wrong place - have to check G here bc otherwise why even double-loop
            elif guess_char in true_word_copy and color_codes[i] != correct_letter:
                color_codes[i] = partial_letter
                
                # Take first appearance of char in true word, set to _
                yellow_ix = true_word_copy.index(guess_char)
                true_word_copy[yellow_ix] = '_'

            
        #TODO: explain or change why are the colors not self
        color_codes = ''.join(color_codes)

        # Add current guess to list of all guesses
        self.guesses.append((guess, color_codes))

        #Add current-guess's letters to alphabetised list of all unique letters in all guesses
        self.letters = ''.join(sorted(set(''.join([letter for guess, _ in self.guesses for each in guess for letter in each]))))

        #todo - return value?????



        
    def print_board(self):
        #Whitespace to distinguish the header from the guess guess
        print()     

        #Header: all guessed letters, then unguessed
        print("Used:\t", self.letters,\
            "\nUnused:\t", ''.join(sorted(set(alphabet) - set(self.letters))) \
            )

        #Whitespace to distinguish the header from previous guesses
        print()        

        #Show all guesses so far & their colors

        #TODO - add some coloring to the 'c' portion here
            #if c == G then print as green
            #etc
            #maybe there's a color-flag or color-hardtexted, I enumerate/zipped into a triple not duple here
        #TODO - separately - number each line
        for g, c in self.guesses:
            print(g,"\t",c)

        #Whitespace to distinguish the new input line
        print()

        #todo - return ?????



#todo - learn why not to actually do this random within the declaration??
#Choose a word from the wordlist, then start the game
currword = random.choice(wordlist)
game = Game(currword)
game.word

#todo - print rules of the game:
    #length of word/guess
    #num guesses allowed
    #?

while not game.is_game_over():
    game.print_board()
    game.make_guess()

    #todo
    #call print_board after each guess re-prompt?
    #yeah, which means pull the validation out into its own loop that make_guess calls
        #(rename make-guess as process guess?)


    
if game.win:
    print(f"You won! it was {game.word}!")
    #reset the word here
else:
    print(f"You lost! it was {game.word}!")




































# avoid repeat guesses!


#avoid too-long guesses
#also avoid too short guseses






#TODO: add to README that I have colors now but only guaranteed for Mac playbackk in Terminal, default prog. 
####should that be tested on: other term apps, Windows, etc?



######go look at the newcolor.py & do the thing!
