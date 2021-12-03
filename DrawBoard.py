from Pawns import initialStateOfPawns, movePawn, pawnsDict
from Walls import wallDict


pawnsDict = {
    'X': [],
    'O': [],
}

initialStateOfPawns(pawnsDict, (2, 2), (5, 2), (3, 5), (5, 5))

pozicije = list()
tabla = list()


def DrawStart(pawnsPosition: pawnsDict, tableSizeN: int, tableSizeM: int):
    # Ovo se poziva samo za prvo iscrtavanje
    StartingBoardState(tableSizeN, tableSizeM)
    UpdatePawns(pawnsPosition)
    StartingBoard(tableSizeN, tableSizeM)
    AddWalls()
    DrawTable()


def DrawMove(pawnsPosition: pawnsDict, tableSizeN: int, tableSizeM: int):
    # Ovo se poziva za svaki potez
    UpdatePawns(pawnsPosition)
    AddWalls()
    DrawTable()


def StartingBoardState(tableSizeN: int, tableSizeM: int):
    # Pozicije je matrica sa pocetnim stanjima table - prazna mesta
    for i in range(0, tableSizeN):
        red = list()
        for j in range(0, tableSizeM):
            red.append(' ')
        pozicije.append(red)


def UpdatePawns(pawnsPosition: pawnsDict):
    # Dodaju se igraci - ovo se poziva pri svakom pomeranju pesaka
    pozicije[pawnsPosition['X'][0][1] - 1][pawnsPosition['X'][0][0] - 1] = 'X'
    pozicije[pawnsPosition['X'][1][1] - 1][pawnsPosition['X'][1][0] - 1] = 'X'
    pozicije[pawnsPosition['O'][0][1] - 1][pawnsPosition['O'][0][0] - 1] = 'O'
    pozicije[pawnsPosition['O'][1][1] - 1][pawnsPosition['O'][1][0] - 1] = 'O'


def ValidatePawnMove(player: str, pawn: int, newSpot: tuple):
    if (newSpot[1] > len(pozicije)):
        return False
    elif (newSpot[0] > len(pozicije[0])):
        return False

    # new_spot je nova pozicija u matrici sa zidovima, a newSpot je samo u matrici stanja
    newX = newSpot[0] * 2 - 1
    newY = newSpot[1] * 2 - 1
    # oldSpot je stara pozicija u matrici stanja
    oldSpot = pawnsDict[player][pawn - 1]
    # old_spot je stara pozicija u matrici sa zidovima
    oldX = oldSpot[0] * 2 - 1
    oldY = oldSpot[1] * 2 - 1

    # Gore
    if(newSpot[0] < oldSpot[0] and newSpot[1] == oldSpot[1]):
        if(tabla[newX+1][newY] == '===' or tabla[newX+3][newY] == '==='):
            return False

    # Dole
    if(newSpot[0] > oldSpot[0] and newSpot[1] == oldSpot[1]):
        if(tabla[newX-1][newY] == '===' or tabla[newX-3][newY] == '==='):
            return False

    # Levo
    if(newSpot[0] == oldSpot[0] and newSpot[1] < oldSpot[1]):
        if(tabla[newX][newY+1] == ' ||' or tabla[newX][newY+3] == ' ||'):
            return False

    # Desno
    if(newSpot[0] == oldSpot[0] and newSpot[1] > oldSpot[1]):
        if(tabla[newX][newY-1] == ' ||' or tabla[newX][newY-3] == ' ||'):
            return False

    # Dijagonala gore levo
    if newSpot[0] == oldSpot[0] - 1 and newSpot[1] == oldSpot[1] - 1:
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


def AddWalls():
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


def DrawTable():
    # Iscrtava matricu table, treba da se pozove nakon svakog dodavanja zida (AddWalls)
    for i in range(0, len(tabla)):
        for j in range(0, len(tabla[i])):
            print(tabla[i][j], end=" ")
        print('\n')


DrawStart(pawnsDict, 8, 10)
print(ValidatePawnMove('X', 1, (1, 3)))
