"""
Kérj be a felhasználótól egy szöveget.  Alakítsd nagybetűssé!
Az előző szövegről döntsd el, hogy 10 karakternél hosszabb-e?
Ha igen, akkor írd ki a hosszát!
Kérj be egy legalább 3 betűs szót a felhasználótól.
A szavakat addig kérd be, amíg a hossza legalább 3!
Kérj be a felhasználótól egy szöveget. Keresd meg benne az első "a" betűt.
Hány "a" betű van a bekért szövegben?
++ feketeöveseknek: Írd ki, hogy a szöveg egyes betűi hányszor szerepelnek
a szövegben?
___________________________________________________________

Addig kérj be neveket a felhasználótól, amíg @ jelet nem üt le.
A szöveget alakítsd át úgy, hogy a kezdőbetűje mindig nagybetű legyen,
a többi kicsi. (szövegkezelő fvények a w3-on) Tárold a neveket egy listában.
Generálj annyi véletlen számot [1, 100] között, ahány nevet bekértél.
A számok az adott nevű ember korát reprezentálják.
 el a számokat "kor" nevezetű listában.
Írd ki a a legidősebb ember nevét!
"""


"""#1.
szoveg= input("Kérlek, adj meg egy szöveget! ")
"""szoveg= f"No cost too great.No mind to think.No will to break.No voice to cry suffering.Born of God and Void.You shals seal the blinding light that plagues their dreams. You are the Vessel.You are the Hollow Knight."""
print(szoveg.upper())
print(len(szoveg))
#2.
szoveg2= input("Másik szöveg pls: ")
if len(szoveg2) > 10:
    print(f"A szöveg hossza: {len(szoveg2)}")
#3.
szoveg3= input("Kérlek adj meg egy 3. szöveget is! 3 betűs legyen minimum pls! ")
if len(szoveg3) < 3:
    print("Ez egy három karakternél kisebb szöveg! ")
elif len(szoveg3) >= 3:
    print("Köszönöm a szöveget")
#Kérj be egy 3 betűs szót a felhasználótól!
#A szavakat addig kérd be, amíg a hossza legaláb 3!
szovegjo= False
while not szovegjo:
    szoveg = input("Kérek egy 3 betűs szót!")
    if len(szoveg) > 3:
        szovegjo = True

#Input szöveg
#Keresd meg benne az első "a" betűt!
szovegsok= input("Kérek egy szöveget! Megkeresem az 1. a betűt benne! ")
i = 0
while i < len(szovegsok) and szovegsok[i].upper() != "A":
    i += 1
#ciklus vége
if i < len(szovegsok):
    print(f"Van a szövegben \"a\" betű a  {i + 1}. karakteren.")
else:
    print("Nincs a szövegben \"a\" betű.")


# Hány "a" betű van a bekért szövegben?
    #***Házi***

"""Addig kérj be neveket a felhasználótól, amíg @ jelet nem üt le.
A szöveget alakítsd át úgy, hogy a kezdőbetűje mindig nagybetű legyen,
a többi kicsi. (szövegkezelő fvények a w3-on) Tárold a neveket egy listában.
Generálj annyi véletlen számot [1, 100] között, ahány nevet bekértél.
A számok az adott nevű ember korát reprezentálják.
 el a számokat "kor" nevezetű listában.
Írd ki a a legidősebb ember nevét!
"""
#Input amíg @-t nem üt le
sokadik_szoveg = input("Kérlek adj meg ismét egy szöveget! ")
i= 0
while i < len(sokadik_szoveg) and len(sokadik_szoveg[i]) != "@":
    i += 1













