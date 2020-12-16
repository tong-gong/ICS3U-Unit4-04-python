#!/usr/bin/env python3

# Created by Tong Gong
# Created time November 2020
# This is a  "Number Guessing Game" program.

import random


def main():
    # This is the function to play the "Number Guessing Game" program.

    random_number = random.randint(1, 10)   # a number between 1 and 10

    # Input
    userinput = input("Enter the number you guess:")
    print("")

    # Process & output
    try:
        userinput = int(userinput)
        if userinput == random_number:
            print("You are right!")
        elif userinput < 0:
            print("It is not a positive integer.")
        elif userinput != random_number:
            while userinput != random_number:
                userinput = int(userinput)
                if userinput > random_number:
                    print("Too big.")
                    userinput = input("Enter the number you guess:")
                elif 0 <= userinput < random_number:
                    print("Too small.")
                    userinput = input("Enter the number you guess:")
                elif userinput < 0:
                    print("It is not a positive integer.")
                elif userinput == random_number:
                    print("You are right!")
                    break
    except Exception:
        print("It is not an integer")


if __name__ == "__main__":
    main()
