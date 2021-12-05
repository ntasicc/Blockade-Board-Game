from Pawns import initialStateOfPawns, movePawn, pawnsDict
from DrawBoard import DrawStart, DrawMove, ValidatePawnMove, DrawPawnMove
from Walls import placeWall, validWall, wallDict, numOfWalls, initialStateOfWalls


class Game:
    whoseTurnIs = True  # na potezu je X, posle svakog poteza menjati
    WhoPlayFirst = True  # prvi igra igrac/ false-racunar
    n = 0
    m = 0
    brojZidova = 0
    initX1 = tuple()
    initX2 = tuple()
    initO1 = tuple()
    initO2 = tuple()

    def __init__(self, WhoPlayX, dimN, dimM, zidovi, X1: tuple, X2: tuple, O1: tuple, O2: tuple):
        self.WhoPlayFirst = WhoPlayX
        self.n = dimN
        self.m = dimM
        self.brojZidova = zidovi
        self.initX1 = X1
        self.initX2 = X2
        self.initO1 = O1
        self.initO2 = O2

    def IsItGameOver(self):

        for x in pawnsDict['X']:
            if(x == self.initO1 or x == self.initO2):
                print("X won the game")
                return True

        for o in pawnsDict['O']:
            if(o == self.initX1 or o == self.initX2):
                print("O won the game")
                return True


# OVDE JE KRAJ KLASE ZA SAD
firstPlay = input(
    "Uneti True ukoliko prvo igra igrac, pritisnutu Enter ukoliko igra prvo PC: ")
n, m = [int(x) for x in input(
    "Unesite N x M dimenzije table, odvojiti razlommkom: ").split()]
zidovi = int(input("Unesite broj zidova: "))
initxX1, inityX1 = [int(x) for x in input(
    "Unesite x i y koordinate od X1, odvojiti razlommkom: ").split()]
initxX2, inityX2 = [int(x) for x in input(
    "Unesite x i y koordinate od X2, odvojiti razlommkom: ").split()]
initxO1, inityO1 = [int(x) for x in input(
    "Unesite x i y koordinate od Y1, odvojiti razlommkom: ").split()]
initxO2, inityO2 = [int(x) for x in input(
    "Unesite x i y koordinate od Y2, odvojiti razlommkom: ").split()]


Game1 = Game(bool(firstPlay), n, m, zidovi, (initxX1, inityX1),
             (initxX2, inityX2), (initxO1, inityO1), (initxO2, inityO2))

initialStateOfWalls(wallDict, zidovi)
initialStateOfPawns(pawnsDict, (initxX1, inityX1),
                    (initxX2, inityX2), (initxO1, inityO1), (initxO2, inityO2))
DrawStart(pawnsDict, Game1.n, Game1.m)

while True:
    if Game1.whoseTurnIs == True:
        igrac1 = "X"
    else:
        igrac1 = "O"

    Game1.whoseTurnIs = not Game1.whoseTurnIs

    print("Trenutno je na potezu " + igrac1)

    brojPesaka = int(input("Pesak 1 ili 2"))

    vrsta, kolona = [int(x) for x in input(
        "Unesite x i y koordinate zeljenog stanja, razdvojiti razmakom ").split()]

    bojaZida = input("p za horizontalni, z za vertikalni")

    if(numOfWalls(wallDict, igrac1, bojaZida)):

        vrstaZid, kolonaZid = [int(x) for x in input(
            "Unesite x i y koordinate zida, razdvojiti razmakom ").split()]

        if ValidatePawnMove(pawnsDict, igrac1, brojPesaka, (vrsta, kolona)) and validWall(igrac1, bojaZida, (vrstaZid, kolonaZid), Game1.n, Game1.m):

            movePawn(pawnsDict, igrac1, brojPesaka, (vrsta, kolona))
            print(pawnsDict)

            placeWall(wallDict, igrac1, bojaZida, (vrstaZid, kolonaZid))
            DrawMove(pawnsDict, bojaZida, (vrstaZid, kolonaZid),
                     igrac1, brojPesaka, (vrsta, kolona))
    else:
        if ValidatePawnMove(pawnsDict, igrac1, brojPesaka, (vrsta, kolona)):
            movePawn(pawnsDict, igrac1, brojPesaka, (vrsta, kolona))
            DrawPawnMove(pawnsDict, igrac1, brojPesaka, (vrsta, kolona))

    if Game1.IsItGameOver():
        break
