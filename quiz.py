# CREATE-A-QUIZ ASSIGNMENT

print("WELCOME TO THE FRENCH HISTORY QUIZ")

score = 0

# input

testq1 = input("1. What year did the French Revolution begin? Answer as a 4 digit number.\n Q1 Answer: ")
if testq1 == "1789":
    print("Correct")
    score += 1
else:
    print("Incorrect")

testq2 = input("2. Fill in the blank: The storming of ___\n Q2 Answer: ")
if testq2.lower() == "bastille":
    print("Correct")
    score += 1
else:
    print("Incorrect")

testq3 = input("What year was the directory formed? Answer as a 4 digit number.\n Q3 Answer: ")
if testq3 == "1795":
    print("Correct")
    score += 1
else:
    print("Incorrect")

testq4 = input("Who crowned themselves emperor after the French Revolution?\n Q4 Answer: ")
if testq4.lower() == "napoleon":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# output

result = (score / 4) * 100

print("YOUR RESULTS:\n" + str(score) + " / 4\n" + str(result) + "%")

if score == 3:
    print("Almost there!")
elif score == 2:
    print("Better luck next time!")
elif score < 2:
    print("You need to study!")
else:
    print("Well done!")