

class Kosar():
    """
    Egyetlen vásárlás adatait kezelő osztály.

    Az osztály attribútumai:
        - a kosárban lévő árucikkek (név-mennyiség párok)
        - a vásárlás összege
    """


    def __init__(self, termekek: dict[str, int]) -> None:
        """
        A kosár létrehozásakor beállítja az osztály attribútumait.
        """
        self.termekek=termekek

    def osszeg_lekerdezese(self, vasarolt:list) -> int:
        """
        A vásárlás összegének lekérdezése.

        :return: A vásárlás összege Ft-ban.
        """
        ar = 0

        for i in range(len(vasarolt)):
            if vasarolt[i][1] > 0:
                if (vasarolt[i][1] == "1"):
                    ar += 1000
                elif (vasarolt[i][1] == "2"):
                    ar += 900
                elif (vasarolt[i][1] >= 3):
                    ar += 800

        return ar

    def termekek_lekerdezese(self) -> dict[str, int]:
        """
        Az árucikk-mennyiség párok lekérdezése.

        :return: Az árucikkek nevei és mennyiségei.
        """


    def termekek_szamanak_lekerdezese(self, vasarolt:list) -> int:
        """
        A kosárban lévő termékek számának lekérdezése.

        :return: Hány darab termék van a kosárban.
        """

        osszestermek = 0
        for i in range(len(vasarolt)):
            osszestermek += vasarolt[i][1]

        return osszestermek

    def arucikk_mennyisegenek_lekerdezese(self, arucikk: str) -> int:
        """
        Egy árucikknek a kosárban megtalálható mennyiségének lekérdezése.

        :param arucikk: A vizsgált árucikk neve.
        :return: A vizsgált árucikk mennyisége a kosárban.
        """


    def kosar_tartalmanak_kiiratasa(self, vasarolt:list) -> None:
        """
        Kiírja a kosár tartalmát a konzolra.
        """

        print("A kosár tartalma: \n")
        for i in range(len(vasarolt)):
            print(f"{vasarolt[i][1]} {vasarolt[i][0]}")