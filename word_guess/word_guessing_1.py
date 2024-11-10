# a simple word guessing game
import random


def main():
    print("\n***** this is a word guesser game *****\n")
    print("create a list of words, the computer will choose one, and you need to guess which one!\n")
    num_words = get_num_words()
    word_list = fill_list(num_words)
    target_word = random.choice(word_list)
    
    i = 1
    while True:
        user_word = get_user_choice(word_list)
        print("\n")
        if user_word == target_word:
            if i == 1:
                print(f"congrats, you guessed it! you needed 1 try.")
            else:
                print(f"congrats, you guessed it! you needed {i} tries.")
            break
        else:
            for l in target_word:
                if l in user_word:
                    print(l, end="")
                else:
                    print("_", end="")
            print("\n")
            i += 1
            continue
        

def get_num_words():
    while True:
        try:
            num_words = int(input("how many words do you want to play with? "))
        except ValueError:
            print("you need to think of a number!")
            continue
        return num_words
    

def fill_list(num):
    words = []
    for n in range(num):
        while True:
            word = input(f"what is word nr. {n + 1}? ")
            if word not in words:
                words.append(word.lower())
                break
            else:
                print("this is already in the list!")
                continue
    return words


def get_user_choice(words):
    while True:
        user_word = input("what is your choice? ")
        if user_word in words:
            return user_word
        else:
            print("the word is not among those you wrote earlier!")
            continue


if __name__ == "__main__":
    main()

