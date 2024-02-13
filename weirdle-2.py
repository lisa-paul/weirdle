#!/usr/bin/env python
# coding: utf-8


#wierdle is wordle but OOP during classtime today
 
#todo
    # discplay all prov letters guessed &/or the entire alphabet
    #before the "all guesses", do:
        #PREV GUESS: print allguesses.aplahabeetzied

    #TRY AGIN if current guess has already been used
    #TRY AGAIN if guess not in the word list

    #TRY AGIN if too short guess
    #TRY AGAIN if too-long guess

    
    #actual terminal colors?

    #script it to run w less typing eg no  "python3"

    
    
    
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

        # Validate that guess is not empty
        guess = []
        while not guess:
            guess = input("Enter a word: ").upper().strip()

        
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


        #hay what if modelled on later for loop & do a "for g,c" but ignore the c

        #Convert/add current-guess's letters to alphabetised list of all unique letters in all guesses
        self.letters = ''.join(sorted(set(''.join([letter for guess, _ in self.guesses for each in guess for letter in each]))))



#        #TODO: only walk thru & add the latest words' guess???
#        #increase efficiency
 
        


    def print_board(self):

        #Show all guessed letters, then unguessed
        print(self.letters,"\t",
            ''.join(sorted(set(alphabet) - set(self.letters)))
            )



        #Show all guesses & their colors
        for g, c in self.guesses:
            print(f"{g}\t{c}")



#tims was a bit different here, since not printing a whole codeblock
#just coloring the guess itself: one column should be output:
        # for guess, colors in self.guesses:
        #     for guess_char, color_char in zip(guess, colors):
        #         if color_char == 'X':
        #             print(guess_char, end=' ')
        #         elif color_char == 'Y':
        #             print(yellow(guess_char), end=' ')
        #         elif color_char == 'G':
        #             print(green(guess_char), end=' ')



        #add whitespace to distinguish the new input line
        print()



#todo - learn why not to actually do the random within the init??

#Choose a word from the wordlist, then start the game
currword = random.choice(wordlist)
game = Game(currword)
game.word



while not game.is_game_over():
    game.make_guess()
    game.print_board()
    
if game.win:
    print(f"You won! it was {game.word}!")
    #reset the word here
else:
    print(f"You lost! it was {game.word}!")
































