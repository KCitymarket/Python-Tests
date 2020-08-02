import time
import random

def trolli():
    yritykset = 0
    luku = 0
    while luku != 50:
        luku = (random.randint(0, 100))
        yritykset = yritykset + 1
        print(luku)
        if luku == 50:
            print ("jes tos on:", luku, "siinä meni", yritykset, "kertaa")
            time.sleep(3)


trolli()