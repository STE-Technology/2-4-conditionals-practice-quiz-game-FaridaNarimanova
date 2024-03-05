"""
File: quiz.py
Author: Name
Date: 2024/03/04
Description: This program  asks the user a series of questions and checks their answers. 
After all the questions have been answered, the program  displays the final score.

"""
# Name of the game
print("Multiple - Choice Quiz Game")

#Initial score of the user
score = 0

# I output fist question
print("1. What is the capital of Azerbaijan?")
print("(a) Ankara")
print("(b) Baku")
print("(c) Istanbul")
# Assign its correct answer, and ask user for answer
correct_answer = "b"
user_answer = input("My answer is: ")

# "If" statemnt indicates correct answer(b), "else" indicates other responds(b,c), and count of scores
if user_answer == correct_answer:
    print("Correct!")
    score = score + 1
else:
    print("Wrong.")

# I output second question with options, and if statements 
print("2. Where is Azerbaijan located?")
print("(a) In Europe")
print("(b) Next to Mexico")
print("(c) In the region of the southern Caucasus Mountains.")
correct_answer = "c"
user_answer = input("My answer is: ")

if user_answer == correct_answer:
    print("Correct!")
    score = score + 1
else:  
    print("Wrong.")

print("3. What is the common religion in Azerbaijan?")
print("(a) Christianity")
print("(b) Islam")
print("(c) Judaism")
correct_answer = "b" 
user_answer = input("My answer is: ")

if user_answer == correct_answer:
    print("Correct!")
    score = score + 1
else:
    print("Wrong.")

print("Quiz is completed!")
scores = round(score / 3) * 100
print("You answered " + str(score)  +   " out of 3 questions correctly. So, your score is " + str(scores) + "%")
