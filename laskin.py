def plus():
    eka = int(input("anna eka numero: "))
    toka = int(input("anna toka numero: "))
    plussa = eka + toka
    print( eka, "+", toka, "=", plussa)
    valinta()

def minus():
    eka = int(input("anna eka numero: "))
    toka = int(input("anna toka numero: "))
    miinus = eka - toka
    print( eka, "-", toka, "=", miinus)
    valinta()

def jako():
    eka = int(input("anna eka numero: "))
    toka = int(input("anna toka numero: "))
    jaakko = eka / toka
    print( eka, "/", toka, "=", jaakko)
    valinta()

def tulo():
    eka = int(input("anna eka numero: "))
    toka = int(input("anna toka numero: "))
    tuulo = eka * toka
    print( eka, "*", toka, "=", tuulo)
    valinta()


def valinta():
     print("valitse minkä haluut")
     print("\n 1 - yhteenlasku 2 - erotus 3 - jako 4 - tulo")
     valiu = input()
     
     if valiu == "1":
         plus()
     elif valiu == "2":
         minus()
     elif valiu == "3":
         jako()
     elif valiu == "4":
         tulo()
     else:
        print("valitte oikee numerro")
        valinta()
    


valinta()