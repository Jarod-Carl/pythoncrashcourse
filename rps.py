import random

def get_user_input():
    
    valid_input = False
    while not valid_input:
        user_input = input("Rock(0) Paper(1) Scissors(2) or q to quit: ")
        if user_input == "q":
            return user_input
        elif user_input == "0" or user_input == "1" or user_input == "2" or user_input == "q":        
            valid_input = True
            return int(user_input)
        else:
           print("Invalid Input")


def check_win(user, comp):
    #0 rock 1 paper 2 scissors
    if user == comp:
        return "Tie"
    elif user == 0 and comp == 2:
        return "Win"
    elif user == 1 and comp == 0:
        return "Win"
    elif user == 2 and comp == 2:
        return "Win"
    elif user == 0 and comp == 1:
        return "Loss"
    elif user == 1 and comp == 2:
        return "Loss"
    elif user == 2 and comp == 0:
        return "Loss"
    
def update_score(result):
    global user_score
    global comp_score
    if result == "Win":
        user_score += 1
    elif result == "Loss":
        comp_score += 1



user_score = 0
comp_score = 0


game_going = True
while game_going:
    options = ["Rock", "Paper", "Scissors"]
    
    user_input = get_user_input()
    if user_input == "q":
        break
    comp_input = random.randint(0, 2)

    #0>2 1>0 2>1 Win Conditions
    result = check_win(user_input, comp_input)
    
    print(f"Computer chose ", options[comp_input])
    print(f"You chose ", options[user_input])
    print(f"You ", result)
    update_score(result)

    print(f"You have ", user_score, "point(s)!")

    

    #game_going = False
