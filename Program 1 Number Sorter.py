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
First, Second, Third, Fourth = startup()
ordering()