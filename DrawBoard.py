from Pawns import pawnsDict, initialStateOfPawns
from Walls import wallDict


pozicije = list()
tabla = list()


def DrawStart(pawnsPosition: dict, tableSizeN: int, tableSizeM: int):
    # Ovo se poziva samo za prvo iscrtavanje
    StartingBoardState(tableSizeN, tableSizeM)
    DrawPawns(pawnsPosition)
    StartingBoard(tableSizeN, tableSizeM)
    DrawWalls()
    DrawTable()


def DrawMove(pawnsPosition: dict, color: str, position: tuple):
    # Ovo se poziva za svaki potez
    DrawPawns(pawnsPosition)
    AddWall(color, position)
    DrawTable()


def StartingBoardState(tableSizeN: int, tableSizeM: int):
    # Pozicije je matrica sa pocetnim stanjima table - prazna mesta
    for i in range(0, tableSizeN):
        red = list()
        for j in range(0, tableSizeM):
            red.append(' ')
        pozicije.append(red)


def DrawPawns(pawnsPosition: dict):
    # Dodaju se igraci - ovo se poziva pri svakom pomeranju pesaka
    pozicije[pawnsPosition['X'][0][1] - 1][pawnsPosition['X'][0][0] - 1] = 'X'
    pozicije[pawnsPosition['X'][1][1] - 1][pawnsPosition['X'][1][0] - 1] = 'X'
    pozicije[pawnsPosition['O'][0][1] - 1][pawnsPosition['O'][0][0] - 1] = 'O'
    pozicije[pawnsPosition['O'][1][1] - 1][pawnsPosition['O'][1][0] - 1] = 'O'


# Ovo postoji i na dnu ValidatePawns, ako dole ostane ovde treba da se obrise
def UpdatePawns(pawnsPosition: dict, player: str, pawn: int, newSpot: tuple):
    newX = newSpot[0] * 2 - 1
    newY = newSpot[1] * 2 - 1
    oldSpot = pawnsPosition[player][pawn - 1]

    oldX = oldSpot[0] * 2 - 1
    oldY = oldSpot[1] * 2 - 1

    # Brise se sa stare pozicije i unosi na novu
    # NE MENJA POZICIJE U PAWNS DICT!!!!
    tabla[oldX][oldY] = " "
    tabla[newX][newY] = player

    pozicije[oldSpot[0] - 1][oldSpot[1] - 1] = " "
    pozicije[newSpot[0] - 1][newSpot[1] - 1] = player


def ValidatePawnMove(pawnsPosition: dict, player: str, pawn: int, newSpot: tuple):

    # new_spot je nova pozicija u matrici sa zidovima, a newSpot je samo u matrici stanja
    newX = newSpot[0] * 2 - 1
    newY = newSpot[1] * 2 - 1
    # oldSpot je stara pozicija u matrici stanja
    oldSpot = pawnsPosition[player][pawn - 1]

    oldX = oldSpot[0] * 2 - 1
    oldY = oldSpot[1] * 2 - 1

    # Proverava da li je nova pozicija van granica table
    if (newSpot[1] > len(pozicije)):
        return False
    elif (newSpot[0] > len(pozicije[0])):
        return False
    # Gore
    if(newSpot[0] < oldSpot[0] and newSpot[1] == oldSpot[1]):
        if(tabla[newX+1][newY] == '===' or tabla[newX+3][newY] == '==='):
            return False
    # Dole
    elif(newSpot[0] > oldSpot[0] and newSpot[1] == oldSpot[1]):
        if(tabla[newX-1][newY] == '===' or tabla[newX-3][newY] == '==='):
            return False
    # Levo
    elif(newSpot[0] == oldSpot[0] and newSpot[1] < oldSpot[1]):
        if(tabla[newX][newY+1] == ' ||' or tabla[newX][newY+3] == ' ||'):
            return False
    # Desno
    elif(newSpot[0] == oldSpot[0] and newSpot[1] > oldSpot[1]):
        if(tabla[newX][newY-1] == ' ||' or tabla[newX][newY-3] == ' ||'):
            return False

    # Dijagonala gore levo
    elif newSpot[0] == oldSpot[0] - 1 and newSpot[1] == oldSpot[1] - 1:
        if ((tabla[newX][newY + 1] == ' ||' and tabla[newX + 2][newY + 1] == ' ||') or
            (tabla[newX + 1][newY] == '===' and tabla[newX + 1][newY + 2] == '===') or
            (tabla[newX][newY + 1] == ' ||' and tabla[newX + 1][newY] == '===') or
                (tabla[newX + 2][newY + 1] == ' ||' and tabla[newX + 1][newY + 2] == '===')):
            return False
    # Dijagonala gore desno
    elif newSpot[0] == oldSpot[0] - 1 and newSpot[1] == oldSpot[1] + 1:
        if ((tabla[newX][newY - 1] == ' ||' and tabla[newX + 2][newY - 1] == ' ||') or
            (tabla[newX + 1][newY] == '===' and tabla[newX + 1][newY - 2] == '===') or
            (tabla[newX][newY - 1] == ' ||' and tabla[newX + 1][newY] == '===') or
                (tabla[newX + 2][newY - 1] == ' ||' and tabla[newX + 1][newY - 2] == '===')):
            return False
    # Dijagonala dole desno
    elif newSpot[0] == oldSpot[0] + 1 and newSpot[1] == oldSpot[1] + 1:
        if ((tabla[newX - 2][newY - 1] == ' ||' and tabla[newX][newY - 1] == ' ||') or
            (tabla[newX - 1][newY - 2] == '===' and tabla[newX - 1][newY] == '===') or
            (tabla[newX][newY - 1] == ' ||' and tabla[newX - 1][newY] == '===') or
                (tabla[newX - 2][newY - 1] == ' ||' and tabla[newX - 1][newY - 2] == '===')):
            return False
    # Dijagonala dole levo
    elif newSpot[0] == oldSpot[0] + 1 and newSpot[1] == oldSpot[1] - 1:
        if ((tabla[newX - 2][newY + 1] == ' ||' and tabla[newX][newY + 1] == ' ||') or
            (tabla[newX - 1][newY] == '===' and tabla[newX - 1][newY + 2] == '===') or
            (tabla[newX][newY + 1] == ' ||' and tabla[newX - 1][newY] == '===') or
                (tabla[newX - 2][newY + 1] == ' ||' and tabla[newX - 1][newY + 2] == '===')):
            return False

    # Brise se sa stare pozicije i unosi na novu
    # NE MENJA POZICIJE U PAWNS DICT!!!!
    tabla[oldX][oldY] = " "
    tabla[newX][newY] = player

    pozicije[oldSpot[0] - 1][oldSpot[1] - 1] = " "
    pozicije[newSpot[0] - 1][newSpot[1] - 1] = player

    return True
    #movePawn(pawnsDict, player, pawn, newSpot)


def StartingBoard(tableSizeN: int, tableSizeM: int):
    # Tabla je matrica koja ce da se stampa, sadrzi igrace, prazna polja i zidove
    newTableSizeN = tableSizeN * 2 + 1
    newTableSizeM = tableSizeM * 2 + 1
    for i in range(0, newTableSizeN):
        red = list()
        if (i % 2 == 0):
            for j in range(0, newTableSizeM):
                if (i == 0 or i == newTableSizeN - 1):
                    red.append(" " if (j % 2 == 0) else "===")
                else:
                    red.append(" " if (j % 2 == 0) else "———")
        else:
            for j in range(0, newTableSizeM):
                red.append(" | " if (j % 2 == 0)
                           else pozicije[(i - 1) // 2][(j - 1) // 2])
            red[0] = "||"
            red[newTableSizeM - 1] = "||"
        tabla.append(red)


def DrawWalls():
    # Dodavanje zidova u tablu koja se iscrtava
    for i in range(0, len(list(wallDict['H']))):
        tabla[(wallDict['H'][i][0] + 1) *
              2][wallDict['H'][i][1] * 2 + 1] = "==="
        tabla[(wallDict['H'][i][0] + 1) *
              2][wallDict['H'][i][1] * 2 + 3] = "==="

    for i in range(0, len(list(wallDict['V']))):
        tabla[wallDict['V'][i][0] * 2 +
              1][(wallDict['V'][i][1] + 1) * 2] = " ||"
        tabla[wallDict['V'][i][0] * 2 +
              3][(wallDict['V'][i][1] + 1) * 2] = " ||"


def AddWall(color: str, position: tuple):
    if color == 'p':
        tabla[(position[0] + 1) * 2][position[1] * 2 + 1] = "==="
    else:
        tabla[position[0] * 2 + 1][(position[1] + 1) * 2] = " ||"


def DrawTable():
    # Iscrtava matricu table, treba da se pozove nakon svakog dodavanja zida (AddWalls)
    for i in range(0, len(tabla)):
        for j in range(0, len(tabla[i])):
            print(tabla[i][j], end=" ")
        print('\n')


initialStateOfPawns(pawnsDict, (1, 1), (2, 2), (3, 3), (4, 4))
DrawStart(pawnsDict, 6, 8)

ValidatePawnMove(pawnsDict, "X", 2, (1, 3))
DrawTable()
