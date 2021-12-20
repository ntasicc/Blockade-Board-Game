from Pawns import initialStateOfPawns, movePawn, pawnsDict
from DrawBoard import DrawStart, DrawMove, DrawTable, ValidatePawnMove, DrawPawnMove, tabla
from Walls import placeWall, validWall, wallDict, numOfWalls, initialStateOfWalls, NumOfColoredWall
import copy


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
while True:
    n, m = [int(x) for x in input(
        "Unesite N x M dimenzije table, odvojiti razmakom: ").split()]
    if(n >= 11 and n <= 22):
        if(m >= 14 and m <= 28):
            break
    print("Uneliste nevazece parametre, minimalna velicina je 11x14 maksimalna 22x28")

zidovi = int(input("Unesite broj zidova: "))
initxX1, inityX1 = [int(x) for x in input(
    "Unesite x i y koordinate od X1, odvojiti razmakom: ").split()]
initxX2, inityX2 = [int(x) for x in input(
    "Unesite x i y koordinate od X2, odvojiti razmakom: ").split()]
initxO1, inityO1 = [int(x) for x in input(
    "Unesite x i y koordinate od Y1, odvojiti razmakom: ").split()]
initxO2, inityO2 = [int(x) for x in input(
    "Unesite x i y koordinate od Y2, odvojiti razmakom: ").split()]


Game1 = Game(bool(firstPlay), n, m, zidovi, (initxX1, inityX1),
             (initxX2, inityX2), (initxO1, inityO1), (initxO2, inityO2))

initialStateOfWalls(wallDict, zidovi)
initialStateOfPawns(pawnsDict, (initxX1, inityX1),
                    (initxX2, inityX2), (initxO1, inityO1), (initxO2, inityO2))
DrawStart(pawnsDict, Game1.n, Game1.m)

WrongParameters = False
numOfTurns = 0

while True:
    if Game1.whoseTurnIs == True:
        igrac1 = "X"
    else:
        igrac1 = "O"
    if(WrongParameters):
        print("Uneli ste nevazece parametre, molimo pokusajte ponovo! ")

    WrongParameters = True

    print("Trenutno je na potezu " + igrac1+": ")

    brojPesaka = int(input("Pesak 1 ili 2: "))

    vrsta, kolona = [int(x) for x in input(
        "Unesite x i y koordinate zeljenog stanja, razdvojiti razmakom: ").split()]
    if(numOfTurns < zidovi*4):
        bojaZida = input("p za horizontalni, z za vertikalni: ")

        if(NumOfColoredWall(wallDict, igrac1, bojaZida) == 0):
            print("Nemate vise zidova zadate boje")
            continue
        vrstaZid, kolonaZid = [int(x) for x in input(
            "Unesite x i y koordinate zida, razdvojiti razmakom: ").split()]

    spotAfterValidation = ValidatePawnMove(
        pawnsDict, igrac1, brojPesaka, (vrsta, kolona))

    if(numOfWalls(wallDict, igrac1, bojaZida)):
        if (spotAfterValidation != False and validWall(igrac1, bojaZida, (vrstaZid, kolonaZid), Game1.n, Game1.m)):

            # Cuvanje starih vrednosti
            oldPawnsDict = copy.deepcopy(pawnsDict)
            oldWallDict = copy.deepcopy(wallDict)
            oldTable = copy.deepcopy(tabla)

            # Odigravanje poteza
            DrawMove(pawnsDict, bojaZida, (vrstaZid, kolonaZid),
                     igrac1, brojPesaka, spotAfterValidation)
            movePawn(pawnsDict, igrac1, brojPesaka, spotAfterValidation)
            placeWall(wallDict, igrac1, bojaZida, (vrstaZid, kolonaZid))

            # Provera da li postoji put do cilja, ako ne postoji vraca se na stare vrednosti i potez se racuna kao nevalidan (na potezu je isti igrac)
            if(astar(tabla, spotAfterValidation, pawnsDict['start'+('O' if igrac1 == 'X' else 'X')][0]) or astar(tabla, spotAfterValidation, pawnsDict['start'+('O' if igrac1 == 'X' else 'X')][1])):
                Game1.whoseTurnIs = not Game1.whoseTurnIs
                WrongParameters = False
                numOfTurns += 1
                DrawTable()
            else:
                pawnsDict = copy.deepcopy(oldPawnsDict)
                wallDict = copy.deepcopy(oldWallDict)
                tabla = copy.deepcopy(oldTable)

    else:

        # Nije potrebno proveravati da li postoji put jer nema vise zidova za postavljanje
        if spotAfterValidation != False:
            DrawPawnMove(pawnsDict, igrac1, brojPesaka, spotAfterValidation)
            movePawn(pawnsDict, igrac1, brojPesaka, spotAfterValidation)
            Game1.whoseTurnIs = not Game1.whoseTurnIs
            WrongParameters = False
            numOfTurns += 1

    if Game1.IsItGameOver():
        break
