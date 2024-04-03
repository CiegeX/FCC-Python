import random


user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number= random.randint(0,2) #rock =0, paper = 1, scissor =2
    computer_pick = options[random_number] # computer choses randomly through the list 
    print ("computer Picked", computer_pick)

    if computer_pick == "rock" and user_input == "paper":
        print("you win!")
        user_wins +=1

    elif computer_pick == "paper" and user_input == "scissors":
        print("you win!")
        user_wins +=1
    
    elif computer_pick == "scissors" and user_input == "rock":
        print("you win!")
        user_wins +=1
    
    else:
        print("you lost!")
        computer_wins +=1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("GoodBye")