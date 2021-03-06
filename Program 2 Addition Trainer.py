# Program 2: Addition Trainer
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random
import sys

def startup(): # Inquire the user if he/she is prepared for the quiz.
    user_option1 = input('Are you prepared to take a quiz? [y/n]: ')
    if user_option1 == 'y': # The user is ready.
        print('You will get 1 point for each correct answer. At the end of the Quiz, your total score will be displayed. Maximum score is 10 points.')
        print('Goodluck!')
        starter_quiz()
    elif user_option1 == 'n': # The user isn't ready.
        print('Be ready next time. Thank you.')
        exit()

def starter_quiz():
    score = 0
    for x in range(10):
        first_number = random.randint(0, 99) # Generate first random number.
        second_number = random.randint(0,99) # Generate second random number.
        questions = (f'{first_number} + {second_number}') 
        user_ans = int(input(f'{x+1}.) {questions} = ')) 
        sys.ans = (first_number + second_number) #Automatically add the two random numbers.
        if user_ans == sys.ans:
            score+=1
            x+=1
            print('Correct answer')
        else:
            if user_ans != sys.ans:
                x+=1
                print(f'Your answer is incorrect. The correct answer is {sys.ans}.')
        if x == 10:
            summary = ('Result:', f'Final Score: {score} out of 10.')
            for result in summary:
                print(result)
            exit()

startup()
starter_quiz()