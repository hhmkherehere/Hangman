import random


def velg_ord():
    try:
        with open('ord.txt', 'r') as f:
            ord_liste = f.read().splitlines()
            if not ord_liste:  # Check if the file is empty
                print("Filen 'ord.txt' er tom!")
                return None
    except FileNotFoundError:
        print("Filen 'ord.txt' ble ikke funnet!")
        return None
    
    return random.choice(ord_liste)


def spill_hangman():
    ordet = velg_ord()

    if ordet is None:
        return  # If no word could be selected, stop the game.

    ordet = ordet.upper()
    gjettet = set()
    forsok = 8

    print("Velkommen til Hangman!")

    while forsok > 0:
        skjerm_ord = [
            bokstav if bokstav in gjettet else '_'
            for bokstav in ordet
        ]
        print("Gjett ordet:", ' '.join(skjerm_ord))
        
        if '_' not in skjerm_ord:
            print("Gratulerer, du klarte det!")
            break

        gjett = input("Gjett en bokstav: ").upper()
    
        # Input validation: ensure it's a single letter
        while len(gjett) != 1 or not gjett.isalpha():
            print("Vennligst tast inn én bokstav.")
            gjett = input("Gjett en bokstav: ").upper()
    
        if gjett in gjettet:
            print("Du har allerede gjettet denne bokstaven.")
        elif gjett in ordet:
            print(f"Bokstaven {gjett} er i ordet!")
            gjettet.add(gjett)
        else:
            print(f"Bokstaven {gjett} er ikke i ordet.")
            gjettet.add(gjett)
            forsok -= 1
            print(f"Du har {forsok} forsøk igjen.")
        print("")  # Blank line for readability

    if forsok == 0:
        print(f"Beklager, du tapte. Ordet var: {ordet}")


if __name__ == "__main__":
    spill_hangman()
