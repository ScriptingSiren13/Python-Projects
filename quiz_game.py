print("Welcome to my science quiz! ")

playing=input("Do you want to play? ") #to check if the user wants to play or not

if playing.lower() !="yes":
    quit()
print("okay! let us play!")
score=0

#asking questions:
#Question 1:
answer=input("Are sharks mammals? ")
if answer.lower()=="no":
    print("Correct!")
    score+=2
else:
    print("Wrong answer!")

#Question 2:
answer=input("What does DNA stand for? ")
if answer.lower()=="deoxyribonucleic acid":
    print("Correct!")
    score+=4
else:
    print("Wrong answer!")

#Question 3:
answer=input("What is the hardest natural substance on Earth ")
if answer.lower()=="diamond":
    print("Correct!")
    score+=1
else:
    print("Wrong answer!")

#Question 4:
answer=input("Which is the main gas that makes up the Earth's atmosphere? ")
if answer.lower()=="nitrogen":
    print("Correct!")
    score+=1
else:
    print("Wrong answer!")

#Question 5:
answer=input("At what temperature are Celsius and Fahrenheit equal? ")
if answer.lower()=="-40":
    print("Correct!")
    score+=2
else:
    print("Wrong answer!")

print("Your score is " + str(score) )
print("You got " + str((score/10) *100) + " %.")