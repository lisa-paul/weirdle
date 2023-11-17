#!/usr/bin/env python
# coding: utf-8



#wierdle is wordle but OOP during classtime today
 
#todo
    #what what too short guess
    #truncate too-long guess
    #no repeat full-guesses allowed
    #verify that guess is a word at all
    
    #actual terminal colors

    #script it
    
    
    
    
# !ls 
#what it's a bash command whee

    

import random

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
        
    def is_game_over(self):
        # If guesses >= 6 -> over
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
        guess = input("Enter a word: ").upper().strip()
        # TODO: More input sanitization
        
        # TODO: Create color_codes
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
    
        # Add guess to self.guesses
        color_codes = ''.join(color_codes)
        self.guesses.append((guess, color_codes))
        
    def print_board(self):
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




        print()




#random real word not hardcode
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
































