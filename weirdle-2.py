#!/usr/bin/env python
# coding: utf-8


#wierdle is wordle but partly OOP during classtime <insert date>
#Later, I added 
    #guessed/unguessed letter display
    #input validation checks

#todo
    #actual terminal colors?
    #script it to run w less typing eg no  "python3"
    #make annotated Jupyter notebook to show smarts
    
    
    
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
            guess = input("Guess a 5-letter word: ").upper().strip()

            # New guess must not be empty
            if not guess:
                continue

            # New guess must not be wrong length
            elif len(guess) != 5:
                print("Word must be 5 letters long.")
                continue

            # Check whether guess is one of the allowed words
            elif guess not in wordlist:
                print("Word was not in the word list.")
                continue 

            # Check if guess is already guessed before
            elif guess in [item[0] for item in self.guesses]:
                print("Word was already guessed.")
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

        #Show all guessed letters, then unguessed
        print("Used:\t", self.letters,\
            "\nUnused:\t", ''.join(sorted(set(alphabet) - set(self.letters))) \
            )

        #Show all guesses so far & their colors
        for g, c in self.guesses:
            print(g,"\t",c)

        #add whitespace to distinguish the new input line
        print()

        #todo - return ?????



#todo - learn why not to actually do this random within the declaration??
#Choose a word from the wordlist, then start the game
currword = random.choice(wordlist)
game = Game(currword)
game.word

#todo - print rules of the game

while not game.is_game_over():
    game.make_guess()
    game.print_board()

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
