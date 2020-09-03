import random
import time

def rps():
    print("ROCK PAPER SCISSORS \n")
    print("everyone knows the rules")
    yourChoice = input()
    
    rule = ("ROCK", "PAPER", "SCISSORS")
    enemyChoice = random.choice(rule)

    print("your choice:", yourChoice)
    time.sleep(1)
    print("your opponent's choice: ", enemyChoice)
    
    if enemyChoice == yourChoice:       
        print("DRAW!")
        time.sleep(1)
    elif enemyChoice == "ROCK" and yourChoice == "PAPER":
        print("YOU WON!")
        time.sleep(1)
    elif enemyChoice == "ROCK" and yourChoice == "SCISSORS":
        print("YOU LOST!")
        time.sleep(1)
    elif enemyChoice == "PAPER" and yourChoice == "ROCK":
        print("YOU LOST!")
        time.sleep(1)
    elif enemyChoice == "PAPER" and yourChoice == "SCISSORS":
        print("YOU Won!")
        time.sleep(1)
    elif enemyChoice == "SCISSORS" and yourChoice == "PAPER":
        print("YOU LOST!")
        time.sleep(1)
    elif enemyChoice == "SCISSORS" and yourChoice == "ROCK":
        print("YOU WON!")
        time.sleep(1)


rps()