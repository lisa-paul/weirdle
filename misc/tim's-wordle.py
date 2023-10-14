import random
from colorama import Fore, Style

words = open('wordlist.txt').readlines()
words = [w.strip() for w in words]

def green(s):
    return Fore.GREEN + s + Style.RESET_ALL

def yellow(s):
    return Fore.YELLOW + s + Style.RESET_ALL

class Game:
    def __init__(self, word=None):
        self.word = word.upper()
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
        
        color_codes = []
        true_word_copy = list(self.word)
        
        # First pass: Mark greens
        for i, guess_char in enumerate(guess):
            if guess_char == true_word_copy[i]:
                color_codes.append('G')
                true_word_copy[i] = '_'
            else:
                color_codes.append('_')
        
        # Second pass: Mark yellows and greys
        for i, guess_char in enumerate(guess):
                
            # Grey if char not in word at all
            if guess_char not in true_word_copy and color_codes[i] != 'G':
                color_codes[i] = 'X'
                
            # Naive: In word, wrong place
            elif guess_char in true_word_copy and color_codes[i] != 'G':
                color_codes[i] = 'Y'
                
                # Take first appearance of char in true word, set to _
                yellow_ix = true_word_copy.index(guess_char)
                true_word_copy[yellow_ix] = '_'
    
        # Add guess to self.guesses
        color_codes = ''.join(color_codes)
        self.guesses.append((guess, color_codes))
        
    def print_board(self):
        for guess, colors in self.guesses:
            for guess_char, color_char in zip(guess, colors):
                if color_char == 'X':
                    print(guess_char, end=' ')
                elif color_char == 'Y':
                    print(yellow(guess_char), end=' ')
                elif color_char == 'G':
                    print(green(guess_char), end=' ')
            print()

random_word = random.choice(words)
game = Game(random_word)

while not game.is_game_over():
    game.make_guess()
    game.print_board()
    
if game.win:
    print(f"You won! The word was {game.word}!")
else:
    print(f"You lost! The word was {game.word}!")