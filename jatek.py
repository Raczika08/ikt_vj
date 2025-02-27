class Jatek:
    def __init__(self, nev, mufaj, ertekeles):
        self.__nev = nev
        self.__mufaj = mufaj
        self.setErtekeles(ertekeles)
    
    def setErtekeles(self, ertekeles):
        self.__ertekeles = ertekeles

    def getNev(self):
        return self.__nev
    def getMufaj(self):
        return self.__mufaj
    def getErtekeles(self):
        return self.__ertekeles
    
    def __str__(self):
        return f"A játék neve: {self.getNev()}, műfaja: {self.getMufaj()}, értékelése: {self.getErtekeles()}"

def leggyakoribbmufajmegtalalasa(jatekok):
    mufajszamlalo = {}
    for jatek in jatekok:
        mufaj = jatek.getMufaj()
        if mufaj in mufajszamlalo:
            mufajszamlalo[mufaj] += 1
        else:
            mufajszamlalo[mufaj] = 1
    leggyakoribbmufaj = max(mufajszamlalo, key=mufajszamlalo.get)
    return leggyakoribbmufaj

def jatekokmentesemufajszerint(jatekok, mufaj):
    fajlnev = f"{mufaj}.txt"
    with open(fajlnev, 'w', encoding='utf-8') as file:
        for jatek in jatekok:
            if jatek.getMufaj() == mufaj:
                file.write(jatek.getNev() + '\n')

def top3jatek(jatekok):
    top3 = sorted(jatekok, key=lambda j: j.getErtekeles())[:3]
    with open("topjatekok.txt", "w", encoding="utf-8") as f:
        for jatek in top3:
            f.write(f"{jatek.getNev()}\n")

jatekok = []
with open('jatekok.txt', "r", encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split(",")
        if len(adatok) == 3:
            jatekok.append(Jatek(adatok[0], adatok[1], adatok[2]))


print("Játékok beolvasása (ENTER-ig):")   
vege = False
while not vege:
    nev = input("Add meg a játék nevét: ")
    if nev == "":
        vege = True
    else:
        db = 0
        for jatek in jatekok:
            if jatek.getNev().lower() == nev.lower():
                db += 1
                print("A játék már szerepel!")
        if db == 0:
            mufaj = input("Add meg a játék műfaját: ")
            ertekeles = input("Add meg a játék értékelését: ")       
            jatekok.append(Jatek(nev, mufaj, ertekeles))

leggyakoribbMufaj = leggyakoribbmufajmegtalalasa(jatekok)
jatekokmentesemufajszerint(jatekok, leggyakoribbMufaj)

top3jatek(jatekok)

print("A program lefutott, az eredmények mentve.")