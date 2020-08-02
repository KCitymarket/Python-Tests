from os import system, name
import time

vanh = []
raha = 5

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls')

def ciggie():
    global vanh
    global raha
    clear()
    print ("Valitse joku näistä ilman mitään syytä        Muut valintasi: ", ', '.join(vanh), "\n")
    print("Rahat = ", raha, "\n")
    print ("1 - Pepsi")
    print ("2 - Valkoinen Monsteri")
    print ("3 - Jaffa")
    print ("4 - 7Up")
    print ("5 - Siti Kola")
    cig = input()


    if cig == "1":
        if raha > 0:
            clear()
            print("Valitsit Pepsin!")
            time.sleep(1)
            vanh.append('Pepsi')
            raha = raha - 1
        else:
            clear()
            print("Sulla ei oo rahaa. Mee pois")
            time.sleep(1)
            quit()
    elif cig == "2":    
        if raha > 0:
            clear()
            print("Valitsit Valkoisen monsterin, hyvä valinta!")
            time.sleep(1)
            vanh.append('Valkoinen Monsteri')
            raha = raha - 1
        else:
            clear()
            print("Sulla ei oo rahaa. Mee pois")
            time.sleep(1)
            quit()
    elif cig == "3":
        if raha > 0:
            clear()
            print("Valitsit Jaffan!")
            time.sleep(1)
            vanh.append("Jaffa")
            raha = raha - 1
        else:
            clear()
            print("Sulla ei oo rahaa. Mee pois")
            time.sleep(1)
            quit()
    elif cig == "4":
        if raha > 0:
            clear()
            print("Valitsit 7Up:in!")
            time.sleep(1)
            vanh.append("7Up")
            raha = raha - 1
        else:
            clear()
            print("Sulla ei oo rahaa. Mee pois")
            time.sleep(1)
            quit()    
    elif cig == "5":
        if raha > 0:
            clear()
            print("mikä sua vaivaa")
            time.sleep(1)
            vanh.append("Siti Kola")
            raha = raha - 1
        else:
            clear()
            print("Sulla ei oo rahaa. Mee pois")
            time.sleep(1)
            quit()
    else: 
        clear()
        print("valitse joku oikee numero pls BTW pidän nää rahat")
        time.sleep(1)
        ciggie()
    
    clear()
    print("haluukko vielä :D")
    print("laita 1 jos haluat lisää, laita 2 jos et halua enempää")
    mor = input()
    
    if  mor == "1":
        ciggie()
    elif mor == "2":
        clear()
        print ("no ei si")
        time.sleep(1)
        quit()

    else:
        clear()
        print("koita laittaa joku noista kahdesta. Ei luulis olevan niin vaikeeta")
        time.sleep(1)
        ciggie()

ciggie()