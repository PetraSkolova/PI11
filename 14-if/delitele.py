""""
while True:
    cislo = int(input("Zadaj číslo (Pre ukoncenie zadaj 0): "))
    if cislo == 0:
        print("Cislo je nula!!!")
        break
    elif cislo % 2 == 0:
            print("Párne")
    else:
            print("Nepárne")
"""

while True:
    cislo = int(input("Zadaj číslo(Pre ukoncenie zadaj 0): "))
    pocet = 0
    print("Delitele:", end=" ")
    for delitel in range(1, cislo + 1):
        if cislo % delitel == 0:
            print( delitel, end=" ")
            pocet += 1     # pocet = pocet + 1
        else:
            cislo % delitel == 2
            print()
            print("Je to prvocislo")
    print()
    print("Pocet delitelov je: ", pocet)
    if cislo == 0:
        break


