from Pawns import initialStateOfPawns, pawnsDict
from Walls import wallDict

initialStateOfPawns(pawnsDict, (2, 2), (5, 2), (3, 5), (5, 5))


def DrawGrid(pawnsPosition: pawnsDict, tableSizeN: int, tableSizeM: int):

    # Pozicije je matrica sa svim pozicijama, tu menjamo pozicije za X i O
    pozicije = list()
    for i in range(0, tableSizeN):
        red = list()
        for j in range(0, tableSizeM):
            red.append(' ')
        pozicije.append(red)
    pozicije[pawnsPosition['X'][0][1] - 1][pawnsPosition['X'][0][0] - 1] = 'X'
    pozicije[pawnsPosition['X'][1][1] - 1][pawnsPosition['X'][1][0] - 1] = 'X'
    pozicije[pawnsPosition['O'][0][1] - 1][pawnsPosition['O'][0][0] - 1] = 'O'
    pozicije[pawnsPosition['O'][1][1] - 1][pawnsPosition['O'][1][0] - 1] = 'O'

    # Tabla sluzi samo za stampanje
    tabla = list()
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

    # Dodavanje zidova
    for i in range(0, len(list(wallDict['V']))):
        tabla[(wallDict['V'][i][0] + 1) *
              2][wallDict['V'][i][1] * 2 + 1] = "==="
        tabla[(wallDict['V'][i][0] + 1) *
              2][wallDict['V'][i][1] * 2 + 3] = "==="

    for i in range(0, len(list(wallDict['H']))):
        tabla[wallDict['H'][i][0] * 2 +
              1][(wallDict['H'][i][1] + 1) * 2] = " ||"
        tabla[wallDict['H'][i][0] * 2 +
              3][(wallDict['H'][i][1] + 1) * 2] = " ||"

    for i in range(0, newTableSizeN):
        for j in range(0, newTableSizeM):
            print(tabla[i][j], end=" ")
        print('\n')


DrawGrid(pawnsDict, 8, 10)
