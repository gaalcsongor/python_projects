# a number guessing game
import random
import re

def main():
    num_1, num_2 = get_user_range()
    target_num = random.randint(num_1, num_2)
    i = 0

    while True:
        user_num = get_user_number()
        i += 1
        if user_num == target_num:
            print(f"Congrats! You have guessed the number in {i} tries.")
            break
        else:
            if user_num > target_num:
                print("Try Again! You guessed too high")
                continue
            else:
                print("Try Again! You guessed too low")
                continue


def get_user_range():
    while True:
        range_number = input("Select a range of whole numbers in this format: A-B: ").strip()
        if not re.match("[0-9]+-[0-9]+", range_number):
            print("You need to input numbers in the given format!")
            continue
        else:
            numbers = range_number.split("-")
            number_1 = int(numbers[0])
            number_2 = int(numbers[1])
            return number_1, number_2
        

def get_user_number():
    while True:
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("You need to input a number!")
            continue
        return guess


if __name__ == "__main__":
    main()