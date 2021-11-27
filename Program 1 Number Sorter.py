# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

# Steps
# 1. Inquire the user the first, second, third, and fourth number.
def startup():
    First = float(input('First Number: '))
    Second = float(input('Second Number: '))
    Third = float(input('Third Number: '))
    Fourth = float(input('Fourth Number: '))
    return First, Second, Third, Fourth

# 2. Use if-else statement to arrange the order of numbers from highest to lowest.
def ordering():
    if First >= Second >= Third >= Fourth: # Proves that the first number is the highest
        print('The descending order of the numbers is:')
        print(First, Second, Third, Fourth)
    elif First >= Second >= Fourth >= Third:
        print('The descending order of the numbers is:')
        print(First, Second, Fourth, Third)
    elif First >= Third >= Second >= Fourth:
        print('The descending order of the numbers is:')
        print(First, Third, Second, Fourth)
    elif First >= Third >= Fourth >= Second:
        print('The descending order of the numbers is:')
        print(First, Third, Fourth, Second)
    elif First >= Fourth >= Second >= Third:
        print('The descending order of the numbers is:')
        print(First, Fourth, Second, Third)
    elif Second >= First >= Third >= Fourth: # Possible the second number is the highest.
        print('The descending order of the numbers is:')
        print(Second, First, Third, Fourth)
    elif Second >= First >= Fourth >= Third:
        print('The descending order of the numbers is:')
        print(Second, First, Fourth, Third)
    elif Second >= Third >= First >= Fourth:
        print('The descending order of the numbers is:')
        print(Second, Third, First, Fourth)
    elif Second >= Third >= Fourth >= First:
        print('The descending order of the numbers is:')
        print(Second, Third, Fourth, First)
    elif Second >= Fourth >= First >= Third:
        print('The descending order of the numbers is:')
        print(Second, Fourth, First, Third)
    elif Second >= Fourth >= Third >= First: 
        print('The descending order of the numbers is:')
        print(Second, Fourth, Third, First)
    elif Third >= First >= Second >= Fourth: # Possible the third number is the highest.
        print('The descending order of the numbers is:')
        print(Third, First, Second, Fourth)
    elif Third >= First >= Fourth >= Second:
        print('The descending order of the numbers is:')
        print(Third, First, Fourth, Second)
    elif Third >= Second >= First >= Fourth:
        print('The descending order of the numbers is:')
        print(Third, Second, First, Fourth)
    elif Third >= Second >= Fourth >= First:
        print('The descending order of the numbers is:')
        print(Third, Second, Fourth, First)
    elif Third >= Fourth >= First >= Second:
        print('The descending order of the numbers is:')
        print(Third, Fourth, First, Second)
    elif Third >= Fourth >= Second >= First: 
        print('The descending order of the numbers is:')
        print(Third, Fourth, Second, First)
    elif Fourth >= First >= Second >= Third: # Possible the fourth number is the highest.
        print('The descending order of the numbers is:')
        print(Fourth, First, Second, Third)
    elif Fourth >= First >= Third >= Second:
        print('The descending order of the numbers is:')
        print(Fourth, First, Third, Second)
    elif Fourth >= Second >= First >= Third:
        print('The descending order of the numbers is:')
        print(Fourth, Second, First, Third)
    elif Fourth >= Second >= Third >= First:
        print('The descending order of the numbers is:')
        print(Fourth, Second, Third, First)
    elif Fourth >= Third >= First >= Second:
        print('The descending order of the numbers is:')
        print(Fourth, Third, First, Second)
    elif Fourth >= Third >= Second >= First: 
        print('The descending order of the numbers is:')
        print(Fourth, Third, Second, First)
    exit()

First, Second, Third, Fourth = startup()
ordering()