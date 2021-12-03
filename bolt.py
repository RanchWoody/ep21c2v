import kosar


class Bolt:
    """
    A vásárlásokat kezelő osztály. Az osztály egyetlen attribútuma a kosarak listája.
    """

    print("3. feladat: Adja meg a vásárlás sorszámát: ")
    sorszam = input()
    sorSzCpy = sorszam
    i = 0
    voltE = True

    vasarolt = [[{""}, {"0"}]]

    '''Ha a megadott pontban F áll akkor onnan balra olvasok tovább F-ig.'''
    if kosar[int(sorszam) - 1] == "F":
        while (kosar[i] != "F"):
            for j in range(len(vasarolt)):
                if (kosar[i] == vasarolt[j][0]):
                    vasarolt[j][0] += 1
                    voltE = False

            if (voltE):
                vasarolt[i][1] = kosar[i]

            i += 1
            voltE = True

    else:
        i = 0
        while (kosar[sorSzCpy] != "F"):
            sorSzCpy -= 1

        while (kosar[sorSzCpy] != "F"):
            for j in range(len(vasarolt)):
                if (kosar[i] == vasarolt[j][0]):
                    vasarolt[j][0] += 1
                    voltE = False

            if (voltE):
                vasarolt[i][1] = kosar[i]

            i += 1
            voltE = True
        '''Ha a megadott pontban nem F-ban áll akkor visszafele halado amíg nem érek egy másik F-hez, majd onnan előrefele lépkedve vizsgálom az elemeket F-ig, ezzel vizsgálva a megadott vásárlást.'''

    def __init__(self):
        """
        A bolt létrehozásakor beállítja az osztály attribútumait.
        """
        pass

    def feladat_1(self, filepath: str) -> None:
        """
        Beolvassa a fájlból a kosarak tartalmát.

        :param filepath: A kosarak tartalmát tartalmazó fájl elérési útvonala.
        """

        be = open("kosar.txt", "r")

        hossz = 0

        while(be.readline() != ""):
            hossz += 1

        kosar = []

        be.tell(0)
        while (be.readline() != ""):
            kosar.append(be.readlines())

        print("1. feladat: A kosar.txt beolvasása.")


    def feladat_2(self, kosar:list, hossz:int) -> None:
        """
        Kiírja, hányan fizettek a pénztárnál.
        """
        vasarlasokSzama = 0

        for i in range(hossz):
            if kosar[i] == "F":
                vasarlasokSzama += 1

        print(f"2. feladat: {vasarlasokSzama} alkalommal fizettek a pénztárnál.")

    def feladat_3(self, kosar:list, hossz:int) -> None:
        """
        Bekéri egy vásárlás sorszámát és kiírja:
            - hány darab árucikk volt a kosárban,
            - mely árucikkekből és milyen mennyiségben vásároltak,
            - a vásárlás összegét.
        """

        print(f"{kosar.termekek_szamanak_lekerdezese()} termék volt a kosárban.")
        kosar.kosar_tartalmanak_kiiratasa()
        print(f"A vásárlás összege: {kosar.osszeg_lekerdezese()}")


    def feladat_4(self, hossz:int) -> None:
        """
        Bekéri egy árucikk nevét és kiírja:
            - melyik vásárlásnál vettek először a termékből
            - melyik vásárlásnál vettek utoljára a termékből
            - összesen hány alkalommal vásároltak a termékből
        """

        print("4. feladat: Adja meg az árucikk nevét: ")
        keresettAru = input()

        elsoVasarlasSorszama = -1
        utolsoVasarlasSorszama = -1
        osszesVasarlasSzama = 0

        for i in range(hossz):
            if(kosar[i] == keresettAru):
                elsoVasarlasSorszama = i
                break

        for i in range(hossz):
            if(kosar[i] == keresettAru):
                utolsoVasarlasSorszama = i
                osszesVasarlasSzama += 1

        print(f"Első vásárlás sorszáma: {elsoVasarlasSorszama}")
        print(f"Utolsó vásárlás sorszáma: {utolsoVasarlasSorszama}")
        print(f"{osszesVasarlasSzama}  alkalommal vásároltak az árucikkből.")


    def feladat_5(self, filepath: str, hossz:int) -> None:
        """
        Elmenti a megadott fájlba a vásárlásonként fizetendő összeget.
        Beolvassa a fájlból a kosarak tartalmát.

        :param filepath: A kosarak tartalmát tartalmazó fájl elérési útvonala.
        """
        ki = open("osszeg.txt")

        vasarolt = [[{""}, {"0"}]]

        vasarlasokSzama = 0

        for i in range(hossz):
            if kosar[i] == "F":
                vasarlasokSzama += 1

        for k in range(vasarlasokSzama):
            while (kosar[i] != "F"):
                for j in range(len(vasarolt)):
                    if (kosar[i] == vasarolt[j][0]):
                        vasarolt[j][0] += 1
                        voltE = False

                if (voltE):
                    vasarolt[i][1] = kosar[i]

                i += 1
                voltE = True

            ar = 0

            for i in range(len(vasarolt)):
                if vasarolt[i][1] > 0:
                    if (vasarolt[i][1] == "1"):
                        ar += 1000
                    elif (vasarolt[i][1] == "2"):
                        ar += 900
                    elif (vasarolt[i][1] >= 3):
                        ar += 800

            ki.write(f"{ar}Ft\n")

