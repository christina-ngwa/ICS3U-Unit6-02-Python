#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: December 2019
# This program finds the greatest number in a list

import random


def find_max(list_of_numbers):
    # this function finds the greatest number
    greatest_num = 0

    # process
    for counter in range(0, len(list_of_numbers)):
        if greatest_num < list_of_numbers[counter]:
            greatest_num = list_of_numbers[counter]

    return greatest_num


def main():
    # this function displays the greatest number

    random_numbers = []
    # output
    print("Let's find the greatest number.")

    # process
    for loop_counter in range(0, 10):
        num = random.randint(1, 100)
        random_numbers.append(num)
    print(random_numbers)

    # call function
    greatest = find_max(random_numbers)

    # output
    print("")
    print("The greatest number from this list is: ", greatest)


if __name__ == "__main__":
    main()
