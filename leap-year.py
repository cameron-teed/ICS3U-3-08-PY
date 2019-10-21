#!/usr/bin/env python3

# Created by: Cameron Teed
# Created on: Oct 2019
# This is program finds out if it's a leap year


def main():
    # calculates if it is a leap year

    # variables
    leap_year = " is not"

    # input
    year = int(input("What is the year: "))

    # process
    # output
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = " is"
        else:
            leap_year = " is"

    print(str(year) + leap_year + " a leap year.")


if __name__ == "__main__":
    main()
