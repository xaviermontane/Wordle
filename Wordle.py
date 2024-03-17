from random import randrange

word_list = ['WHILE', 'DICTS', 'FLOAT', 'RANGE', 'BREAK']

def check_word():
    word = randrange(0, 5)
    word = word_list[word] # Wordle
    word = 'BREAK' # Test var.
    count = 0 # Correct hits
    tries = 6

    while count < 5 and tries > 0:
        print('\n–––––––––––—')
        print(f'You have {tries} tries left.')
        print(f'You have found {count} letters.')
        guess = str(input(f'\nChoose a word: ').upper())
        if len(guess) < 5 or len(guess) > 5:
            print('[!] — Please enter a 5 letter word.')
            continue
        tries -= 1
        
        for char in guess:
            if char in word and word.index(char) == guess.index(char):
                print(f'{char} | √')
                count += 1
                
            elif char in word:
                print(f'{guess[guess.index(char)]} | ≈') # Wrong spot symbol
            else:
                print(f'{char} | X')

    if count == 5: # ??
        print('\nCongratulations, you have solved the Wordle!')

check_word()

"""
How To Play
Guess the Wordle in 6 tries.
Each guess must be a valid 5-letter word.
The color of the tiles will change to show how close your guess was to the word.

Examples:

√
W is in the word and in the correct spot.

≈
I is in the word but in the wrong spot.

X
U is not in the word in any spot.
"""