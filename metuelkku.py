import time
import random

#User chooses a number between 1 and 1000 
#machine outputs random numbers until it gets user input
#then it outputs "Here's your number:(user input) it took (number of tries) tries"

def numRand():
    num = int(input("Minkä numeron haluat arvottavaksi (väliltä 1 - 1000)"))    
    if num > 1000:
        print("liian suuri numero")
        numRand()
    if num < 0:
        print("liian pieni numero")
        numRand()
    yritykset = 0
    luku = 0
    while luku != num:
        luku = (random.randint(0, 1000))
        yritykset = yritykset + 1
        print(luku)
        if luku == num:
            print ("Siinä on numerosi:", luku, "Siinä meni", yritykset, "yritystä")
            time.sleep(3)
            break


numRand()
