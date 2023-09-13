print("Welcome to quiz!")

playing = input("Do you want to play quiz? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's start :)")
score = 0

answer = input("What is quiz? ")
if answer.lower() == "set of questions":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who developed python language? ")
if answer.lower() == "guido van rossum":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which year python languge was developed? ")
if answer.lower() == "1995":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which language python is written in? ")
if answer.lower() == "c":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Is the Earth round? ")
if answer.lower() == "Yesyes":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")

print("do you want to play again? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's start :)")
score = 0