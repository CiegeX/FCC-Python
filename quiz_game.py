print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "Yes":
    quit()

print("Okay ! Let's play :)")
score= 0

answers = input ("What does CPU stand for? ")
if answers.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print ("Incorrect!")

answerz = input ("What does GPU stand for?  ").lower()
if answerz == "graphic processing unit":
    print("Correct!")
    score+=1
else:
    print ("Incorrect!")

answerx = input ("What does RAM stand for? ")
if answerx.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print ("Incorrect!")

answerc = input ("What does PSU stand for? ")
if answerc.lower() == "power supply unit":
    print("Correct!")
    score+=1
else:
    print ("Incorrect!")


    print("You got " + str(score) + "questions correct!")
    print("You got " + str((score/4) *100) + "%.")




    