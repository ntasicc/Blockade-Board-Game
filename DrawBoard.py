from Pawns import initialStateOfPawns, pawnsDict


initialStateOfPawns(pawnsDict, (2, 2), (5, 2), (3, 5), (5, 5))


def DrawGrid(pawnsPosition: pawnsDict, tableSize: int):

    # Pozicije je matrica sa svim pozicijama, tu menjamo pozicije za X i O
    pozicije = list()
    for i in range(0, tableSize):
        red = list()
        for j in range(0, tableSize):
            red.append(' ')
        pozicije.append(red)
    pozicije[pawnsPosition['X'][0][1] - 1][pawnsPosition['X'][0][0] - 1] = 'X'
    pozicije[pawnsPosition['X'][1][1] - 1][pawnsPosition['X'][1][0] - 1] = 'X'
    pozicije[pawnsPosition['O'][0][1] - 1][pawnsPosition['O'][0][0] - 1] = 'O'
    pozicije[pawnsPosition['O'][1][1] - 1][pawnsPosition['O'][1][0] - 1] = 'O'

    # Tabla sluzi samo za stampanje
    tabla = list()
    newTableSize = tableSize * 2 + 1
    for i in range(0, newTableSize):
        red = list()
        if (i % 2 == 0):
            for j in range(0, newTableSize):
                if (i == 0 or i == newTableSize - 1):
                    red.append(" " if (j % 2 == 0) else "===")
                else:
                    red.append(" " if (j % 2 == 0) else "———")
        else:
            for j in range(0, newTableSize):
                red.append(" | " if (j % 2 == 0)
                           else pozicije[(i - 1) // 2][(j - 1) // 2])
            red[0] = "||"
            red[newTableSize - 1] = "||"
        tabla.append(red)

    for i in range(0, newTableSize):
        for j in range(0, newTableSize):
            print(tabla[i][j], end=" ")
        print('\n')


DrawGrid(pawnsDict, 8)
