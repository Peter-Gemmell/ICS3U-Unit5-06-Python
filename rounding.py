#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on March 2022
# This program calculates the circumference of a circle using constants


def round_number(input_number, rounded_by):
    # round number

    # process
    temp = (input_number[0] * (10**rounded_by)) + 0.5
    temp = int(temp)
    temp = temp / (10**rounded_by)

    input_number[0] = temp


def main():
    # this function gets the user input
    list_number = []

    # input
    ask_user_number = input("Enter the number you want to round : ")
    ask_round_by = input("Enter how many decimal places you want to round by : ")

    try:
        input_number = float(ask_user_number)
        list_number.append(input_number)
        rounded_by = int(ask_round_by)
        # call function
        round_number(list_number, rounded_by)
        print("\nThe rounded number is {0}".format(list_number[0]))
    except Exception:
        print("\nInvalid number entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
