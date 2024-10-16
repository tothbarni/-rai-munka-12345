import random
def elso(szam:int):
    while (szam % 2 == 0):
        szam:int = int(input("Adj meg egy páratlan számot : "))

def masodik():
    oszthato = 0
    for i in range(1, 8, 1):
        szam:int = int(random.random()*96 + 5)
        print(szam)
        if szam % 5 == 0:
            oszthato += 1
    return oszthato

def harmadik(szoveg:str, betu:str):
    i = 0
    db:int = 0
    while i < len(szoveg):
        if (szoveg[i] == betu):
            db += 1
        i += 1
    print(f"A szövegben {db}db '{betu}' betú van.")


def negyedik(nev):
    nevek:str = []
    while nev != "@":
        nev:str = input("Adj meg egy nevet : ")
        nevek.append(nev)
    print(f"A felhasználó {len(nevek)} nevet adott meg.")

def otodik(tipp):
    felhasznalo_tippje:str = tipp.lower()
    szam:int = int(random.random()*3)
    szov:str = ""
    if (szam == 1):
        szov = "kő"
    elif (szam == 2):
        szov = "papír"
    elif (szam == 3):
        szov = "olló"


    if (felhasznalo_tippje == "olló") and (szov == 2):
        print("Nyertél.")
    elif (felhasznalo_tippje == "olló") and (szov == 1):
        print("Vesztettél.")
    elif (felhasznalo_tippje == "kő") and (szov == 2):
        print("Vesztettél.")
    elif (felhasznalo_tippje == "kő") and (szov == 3):
        print("Vesztettél.")
    elif (felhasznalo_tippje == "papír") and (szov == 3):
        print("Vesztettél.")
    elif (felhasznalo_tippje == "papír") and (szov == 1):
        print("Nyertél.")
    
    if (felhasznalo_tippje == szov):
        print("Döntetlen.")
