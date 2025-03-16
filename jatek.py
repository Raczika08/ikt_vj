class JATEKOK():
  def __init__(self,nev,mufaj,ertekeles):
    self.__nev = nev
    self.__mufaj = mufaj
    self.__ertekeles = ertekeles
  
  def getNev(self):
    return self.__nev
  def getMufaj(self):
    return self.__mufaj
  def getErtekeles(self):
    return self.__ertekeles


  def __str__(self):
    return f"{self.getNev()},{self.getMufaj()},{self.getErtekeles()}"
  
def beolvas():
  lista = []
  with open("jatek.txt", 'r', encoding="utf-8") as fajl:
    for sor in fajl:
        reszek = sor.strip().split(",")
        j = JATEKOK(reszek[0],reszek[1],(float)(reszek[2]))
        lista.append(j)
    return lista

lista = beolvas()

def maximum_mufaj(lista):
    mufajok = []
    mufaj = []
    for i in lista:
        if i.getMufaj() not in mufajok:
            mufajok.append(i.getMufaj())
    for i in mufajok:
        db = 0
        for j in lista:
            if i == j.getMufaj():
                db += 1
        mufaj.append(i+"-"+(str)(db))
    maxszam = 0
    maxnev = ""
    for i in mufaj:
        reszek = i.split("-")
        if (int)(reszek[1]) > maxszam:
            maxszam = (int)(reszek[1])
            maxnev = reszek[0]
    with open(f'{maxnev}.txt', 'w', encoding="UTF-8") as fajl:
        for i in lista:
            if i.getMufaj() == maxnev:
                print(i, file=fajl)


def top_3(lista):
    rendezett = sorted(lista, key=lambda x: x.getErtekeles(), reverse=True)
    vegig = 0
    top3 = []
    for i in rendezett:
        if vegig <= 0:
            top3.append(i)
            vegig += 1
    return rendezett


def top_3_txt(top3):
   with open('topjatekok.txt', 'w', encoding="UTF-8") as fajl:
      for i in top3:
        print(i, file=fajl)


vegek = False
while not vegek:
    print("\nVálasszd ki az egyik opciot:")
    print("1. Kedvenc játék megadása")
    print("2. Maximum műfaj")
    print("3. Top 3 játék")
    print("4. Kilépés")
    valasztas = input("")
    if valasztas == "1":
        mehet = True
        vege = False
        while not vege:
            lista = beolvas()
            jatek = input("\nMi a kedvenc játékod? ")
            if jatek == "":
                vege = True
            else:
                for i in lista:
                    if jatek == i.getNev():
                        mehet = False
                if mehet == False:
                    print("Ez a játék már benne van a listában!")
                else:
                    with open('jatek.txt', 'a', encoding="UTF-8") as fajl:
                        tipus = input("Mi a játék műfaja? ")
                        ertekeles = (float)(input("Milyen értékelése van a játéknak? "))
                        j = JATEKOK(jatek,tipus,(float)(ertekeles))
                        print(j, file=fajl)
    elif valasztas == "2":
       maximum_mufaj(lista)
       print("A szöveges fájl elkészült! ")
    elif valasztas == "3":
       x = top_3(lista)
       top_3_txt(x)
       print("A szöveges fájl elkészült! ")
    elif valasztas == "4":
        vegek = True
        print("Kilépés...")
    else:
       print("Ilyen opció nem létezik! Probáld ujra!")