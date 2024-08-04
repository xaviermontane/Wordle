from random import choice

word_list = ["WHILE", "DICTS", "FLOAT", "RANGE", "BREAK", "LOOPS", "INPUT", "PRINT", 
  "TUPLE", "LISTS", "STRIN", "FUNCT", "CLASS", "FILES", "ERROR", "RAISE", 
  "LOCAL", "YIELD", "REGEX", "STRIP"]

def play_wordle():
  count = 0
  tries = 6
  word = choice(word_list)
  hits = ["_", "_", "_", "_", "_"]

  print("\nWelcome to Wordle! — The five letter word game")
  while tries > 0:
    print("\n–––––––––––—")
    print(f"You have {tries} tries left.")
    print(f"You have found {count} letters.")

    guess = input("\nChoose a word: ").upper()
    print("–––––––––––—\n")
    if len(guess) != 5 or not guess.isalpha():
      print("[!] — Please enter a 5 letter word.")
      continue
    tries -= 1

    for i, char in enumerate(guess):
      if char == word[i]:
        print(f"{char} | √")
        if char not in hits:
          hits[i] = char
          count += 1
      elif char in word:
        print(f"{char} | ≈")
      else:
        print(f"{char} | X")

    if count == 5:
      print("\nCongratulations, you have solved the Wordle!")
      print(f"The word was: {word.capitalize()}\n")
      break

  if tries == 0 and count < 5:
    print("\nYou have run out of tries!")
    print(f"The word was: {word.capitalize()}\n")
  
  play_again = input("Would you like to play again? (y/n): ").lower()
  if play_again == "y":
      play_wordle()
  else:
    print("\n\nThank you for playing Wordle!\nCredits to Josh Wardle for the original game <3\n")

play_wordle()