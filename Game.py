from Pawns import initialStateOfPawns, pawnsDict
from DrawBoard import DrawStart, DrawMove, ValidatePawnMove, DrawPawnMove
from Walls import validWall

initialStateOfPawns(pawnsDict, (1, 2), (3, 4), (9, 10), (11, 11))


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
                return

        for o in pawnsDict['O']:
            if(o == self.initX1 or o == self.initX2):
                print("O won the game")
                return


# OVDE JE KRAJ KLASE ZA SAD
firstPlay = input(
    "Uneti True ukoliko prvo igra igrac, pritisnutu Enter ukoliko igra prvo PC: ")
n, m = [int(x) for x in input(
    "Unesite N x M dimenzije table, odvojiti razlommkom: ").split()]
zidovi = input("Unesite broj zidova: ")
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
print(Game1.WhoPlayFirst)

Game.IsItGameOver(Game1)
# prvo ispisuje pawnDict zato sto u Pawns.py je pozvana funkcija initialState.. i print isto kao kod JS fazon
