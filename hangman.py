import random

def velg_ord():
    with open('ordliste.txt', 'r') as f:
        ord_liste = f.read().splitlines()
    return random.choice(ord_liste)

def spill_hangman():
    ordet = velg_ord().upper()
    gjettet = set()
    forsok = 8  

    print("Velkommen til Hangman!")
    while forsok > 0:
        skjerm_ord = [bokstav if bokstav in gjettet else '_' for bokstav in ordet]
        print("Gjett ordet:", ' '.join(skjerm_ord))
        
        if '_' not in skjerm_ord:
            print("Gratulerer, du vant!")
            break

        gjett = input("Gjett en bokstav: ").upper()
        if gjett in gjettet:
            print("Du har allerede gjettet denne bokstaven.")
        elif gjett in ordet:
            print(f"Bokstaven {gjett} er i ordet!")
            gjettet.add(guett)
        else:
            print(f"Bokstaven {gjett} er ikke i ordet.")
            gjettet.add(guett)
            forsok -= 1
            print(f"Du har {forsok} forsøk igjen.")

    if forsok == 0:
        print(f"Beklager, du tapte. Ordet var: {ordet}")

if __name__ == "__main__":
    spill_hangman()
