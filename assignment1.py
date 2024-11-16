#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Summer 2023
Program: assignment1.py 
Author: Mitchell Gregoris
ID: 133349191
Email: mgregoris2@myseneca.ca
The python code in this file (a1_[Student_id].py) is original work written by
Mitchell Gregoris. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]

def leap_year_days(month:int, year:int) -> int:
    ''' Calculates how many days are in each month during a leap year 
        Paramters: month:int, year:int
        Returns integer value for how many days in the month for that year
    '''
    month = int(month)
    year = int(year)
    days = 0
    if (month == 1):
        days = 31
    elif (month == 2):
        days = 29
    elif (month == 3):
        days = 31
    elif (month == 4):
        days = 30
    elif (month == 5):
        days = 31
    elif (month == 6):
        days = 30
    elif (month == 7):
        days = 31
    elif (month == 8):
        days = 31
    elif (month == 9):
        days = 30
    elif (month == 10):
        days = 31
    elif (month == 11):
        days = 30
    elif (month == 12):
        days = 31
    return days
    
def non_leap_year_days(month:int, year:int) -> int:
    ''' Calculates how many days are in each month during a NON-leap year 
        Paramters: month:int, year:int
        Returns integer value for how many days in the month for that year
    '''
    month = int(month)
    year = int(year)
    days = 0
    if (leap_year(year) == False): # condition can be removed
        if (month == 1):
            days = 31
        elif (month == 2):
            days = 28
        elif (month == 3):
            days = 31
        elif (month == 4):
            days = 30
        elif (month == 5):
            days = 31
        elif (month == 6):
            days = 30
        elif (month == 7):
            days = 31
        elif (month == 8):
            days = 31
        elif (month == 9):
            days = 30
        elif (month == 10):
            days = 31
        elif (month == 11):
            days = 30
        elif (month == 12):
            days = 31
        return days


def mon_max(month:int, year:int) -> int:
    '''returns the maximum day for a given month. Includes leap year check
        Calculate if the days of the week exceed the days in the month
        If true, increase month +1, Else keep variables

    '''
    month = int(month)
    year = int(year)
    days = 0
    if (month == 1):
        days = 31
    elif (month == 2):
        days = 28
    elif (month == 3):
        days = 31
    elif (month == 4):
        days = 30
    elif (month == 5):
        days = 31
    elif (month == 6):
        days = 30
    elif (month == 7):
        days = 31
    elif (month == 8):
        days = 31
    elif (month == 9):
        days = 30
    elif (month == 10):
        days = 31
    elif (month == 11):
        days = 30
    elif (month == 12):
        days = 31
    return days 
            

def parse_date(date: str) -> int:
    ''' Takes in date string, parses string into our day, month year values
        removes our '-' delimiter, returns integers to pass to other functions
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    return int(year), int(month), int(day)


def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    # Parse given data arguments, remove '-' delimeter, set string values to integer
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    
    tmp_day = day + 1  # next day

    # Calculate if the days of the week exceed the days in the month
    # If true, increase month +1
    # Else keep variables
    if tmp_day > mon_max(month, year):
        to_day = tmp_day % mon_max(month, year)  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    # Calculate if added month exceeds our 12 month calendar
    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date


def usage():
    "Print a usage message to the user"
    ...


def leap_year(year: int) -> bool:
    ''' Every year divisiable by 4 is a leap year,
        Exception for years divisable by 100,
        Exception for every century if they are divisable by 400,
        Accepts int year, returns True if the year is a leap year"
    '''
    leap_flag = False
    tmp_year = year

    if (tmp_year % 400 == 0):
        leap_flag = True
    elif (tmp_year % 100 == 0):
        leap_flag = False
    elif (tmp_year % 4 == 0):
        leap_flag = True
    
    return leap_flag

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    ...

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    ...

if __name__ == "__main__":
    ...