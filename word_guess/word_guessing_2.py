# another iteration of the word guessing game
import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

user_word = []
tries = 0
comp_word = random.choice(words)

user_name = input("what is your name? ")
print(f"Good Luck {user_name}!")
print("Try to guess the characters, you have 12 tries")

for _ in comp_word:
    print("_")

while True:
    end_word_user = set(user_word)
    end_word_comp = str(comp_word).strip("[]'")
    end_word_comp = set(end_word_comp)
    if len(end_word_user) == len(end_word_comp):
        print("congrats! you have won the game!")
        print(f"the word was: {comp_word}")
        break
    
    user_char = input("guess a character: ").lower()
    if user_char in comp_word:
        if user_char not in user_word:
            user_word.append(user_char)
        else:
            print("you already added this letter earlier!")
            continue
    
    for l in comp_word:
        if l in user_word:
            print(l)
        else:
            print("_")
    
    tries += 1
    print(f"attempts left: {12 - tries}")
    
    if tries > 11:
        print("you have lost the game, sorry")
        break 
            