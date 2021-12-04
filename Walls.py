wallDict = {
    'V': [(1, 2)],
    'H': [],
    'numX': [],
    'numO': []
}
# u numX/O se stavlja list [V,H] koja cuva broj zidova igraca


def initialStateOfWalls(dictionary: dict, k: int):
    dictionary['numX'] = [k, k]
    dictionary['numO'] = [k, k]


# zeleni vertikalno, plavi horizontalno


def placeWall(dictionary: dict, player: str, color: str, newSpot: tuple):
    dictionary['V' if color == 'z' else 'H'].append(newSpot)
    dictionary['numX' if player ==
               'X' else 'numO'][0 if color == 'z' else 1] -= 1


# placeWall(wallDict, 'X', 'z', (5, 5))
#placeWall(wallDict, 'O', 'p', (2, 0))


# tableSizeM i N ukloniti za sad su samo tu
def validWall(color: str, newsSpot: tuple, tableSizeN, tableSizeM):

    if (newsSpot[0] > tableSizeN-2) or (newsSpot[1] > tableSizeM-2):
        return False
    if(color == 'z'):
        for x in wallDict['V']:
            if ((x == newsSpot) or
                (x[1] == newsSpot[1] and x[0] == newsSpot[0]+1) or
                    (x[1] == newsSpot[1] and x[0] == newsSpot[0] - 1)):
                return False
        for x in wallDict['H']:
            if(newsSpot[0]+1 == x[0] and newsSpot[1]-1 == x[1]):
                return False
        print("TRUE")
        return True
    if(color == 'p'):
        for x in wallDict['H']:
            if ((x == newsSpot) or
                (x[0] == newsSpot[0] and x[1] == newsSpot[1]+1) or
                    (x[0] == newsSpot[0] and x[1] == newsSpot[1]-1)):
                return False
        for x in wallDict['V']:
            if(newsSpot[0]-1 == x[0] and newsSpot[1]+1 == x[1]):
                return False
        print("TRUE")
        return True
