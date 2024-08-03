from random import randrange

word_list = ["WHILE", "DICTS", "FLOAT", "RANGE", "BREAK"]

word = randrange(0, 5)
word = word_list[word]  # Wordle

def check_word():
  count = 0  # Correct hits
  tries = 6 # Available tries
  hits = ["_", "_", "_", "_", "_"] # User progress

  while count < 5 and tries > 0:
    print("\n–––––––––––—")
    print(f"You have {tries} tries left.")
    print(f"You have found {count} letters.")

    guess = str(input("\nChoose a word: ").upper()) # User input
    print("–––––––––––—\n")
    if len(guess) < 5 or len(guess) > 5 or guess.isalpha() is False:
      print("[!] — Please enter a 5 letter word.")
      continue
    tries -= 1

    for char in guess:
      if char in word and word.index(char) == guess.index(char):
        print(f"{char} | √") # Output purpose only
        # Insert and count logic
        if char not in hits:
          hits.insert(word.index(char), char)
          count += 1
      elif char in word:
        print(f"{guess[guess.index(char)]} | ≈")  # Wrong spot symbol
      else:
        print(f"{char} | X")

  if count == 5:
    print("\nCongratulations, you have solved the Wordle!")
    print(f"The word was: {word.capitalize()}\n") 

check_word()