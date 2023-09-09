import random


def dice():
    try:
        range_ = int(input("Enter dice range:from 1 to "))
        dice_num = random.randint(1, range_)
        print(f"Dice Number: {dice_num}")
    except ValueError:
        print("Please enter a number.")


dice()
