from random import randrange

word_list = ['WHILE', 'DICTS', 'FLOAT', 'RANGE', 'BREAK']


def check_word():
  word = randrange(0, 5)
  word = word_list[word]  # Wordle
  word = 'BREAK'  # Test var.
  count = 0  # Correct hits
  tries = 6
  hits = []

  while count < 5 and tries > 0:
    print('\n–––––––––––—')
    print(f'You have {tries} tries left.')
    print(f'You have found {count} letters.')
    guess = str(input('\nChoose a word: ').upper())
    if len(guess) < 5 or len(guess) > 5 or guess.isalpha() is False:
      print('[!] — Please enter a 5 letter word.')
      continue
    tries -= 1

    for char in guess:
      if char in word and word.index(char) == guess.index(char):
        print(f'{char} | √')
        count += 1
        hits.append(char)

        if char in hits:  # In progress
          print('Check')
      elif char in word:
        print(f'{guess[guess.index(char)]} | ≈')  # Wrong spot symbol
      else:
        print(f'{char} | X')

  if count == 5:  # ??
    print('\nCongratulations, you have solved the Wordle!')


check_word()