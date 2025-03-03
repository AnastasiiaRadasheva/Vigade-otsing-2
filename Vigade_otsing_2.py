print("*** ARVUDE MÄNG ***")  # Tervitussõnum
print()

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Küsime kasutajalt täisarvu ja kontrollime sisendi korrektsust
while True:
    try:
        a = abs(int(input("Sisesta täisarv => ")))  # Sisesta täisarv
        break  # Kui sisestus on korrektne, väljumetsüklis
    except ValueError:
        print("See ei ole täisarv")  # Veateade vale sisendi korral

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a == 0:
    print("Nulliga pole mõtet midagi teha")  # Kui sisestatud arv on 0, lõpetame
else:
    print("Loendame, mitu on paaris ja mitu paaritut numbrit")
    print()
    
    c = b = a  # Salvestame algse arvu koopia
    paaris = 0  # Paarisarvude loendur
    paaritu = 0  # Paaritute arvude loendur
    
    while b > 0:
        if b % 2 == 0:  # Kontrollime, kas number on paaris
            paaris += 1  # Suurendame paarisarvude loendurit
        else:
            paaritu += 1  # Suurendame paaritute arvude loendurit
        b = b // 10  # Eemaldame viimase numbri arvust
    
    print("Paaris numbrid:", paaris)
    print("Paaritud numbrid:", paaritu)
    print()
    
    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    # Pöörame sisestatud arvu ümber
    print("*Ümberpöörame* sisestatud arvu")
    print()
    
    b = 0  # Muutuja ümberpööratud arvu salvestamiseks
    while a > 0:
        number = a % 10  # Saame viimase numbri
        a = a // 10  # Eemaldame viimase numbri
        b = b * 10 + number  # Moodustame ümberpööratud arvu
    
    print("*Ümberpööratud* arv", b)
    print()
    
    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    # Tõestame Syracuse hüpoteesi (Collatzi hüpotees)
    print("Tõestame teoreemi")
    print()
    
    while c != 1:
        if c % 2 == 0:  # Kui arv on paarisarv
            print(c, "- Paaris arv, Jagame 2.")
            c = c // 2  # Jagame 2-ga
        else:  # Kui arv on paaritu
            print(c, "- Paaritu arv. Korrutame 3, liidame 1 ja jagame 2.")
            c = (3 * c + 1) // 2  # Korrutame 3-ga, liidame 1 ja jagame 2-ga
    
    print("1 - Teoreem on tõestatud")
    print()
    print("Press any key to continue . . .")
