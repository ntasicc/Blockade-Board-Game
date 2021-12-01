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


initialStateOfWalls(wallDict, 3)

# zeleni vertikalno, plavi horizontalno


def placeWall(dictionary: dict, player: str, color: str, newSpot: tuple):
    dictionary['V' if color == 'z' else 'H'].append(newSpot)
    dictionary['numX' if player ==
               'X' else 'numO'][0 if color == 'z' else 1] -= 1


# placeWall(wallDict, 'X', 'z', (5, 5))
#placeWall(wallDict, 'O', 'p', (2, 0))


# tableSizeM i N ukloniti za sad su samo tu
def validWall(color: str, newsSpot: tuple, tableSizeN, tableSizeM):
    if(newsSpot[0] > tableSizeN-2):
        return False
    elif(newsSpot[1] > tableSizeM-2):
        return False
    if(color == 'z'):
        for x in wallDict['V']:
            if(x == newsSpot):
                return False
            if(x[1] == newsSpot[1] and x[0] == newsSpot[0]+1):
                return
            if(x[1] == newsSpot[1] and x[0] == newsSpot[0] - 1):
                return False
        for x in wallDict['H']:
            if(newsSpot[0]+1 == x[0] and newsSpot[1]-1 == x[1]):
                return False
        print("TRUE")
        return True
    if(color == 'p'):
        for x in wallDict['H']:
            if(x == newsSpot):
                return False
            if(x[0] == newsSpot[0] and x[1] == newsSpot[1]+1):
                return False
            if(x[0] == newsSpot[0] and x[1] == newsSpot[1]-1):
                return False
        for x in wallDict['V']:
            if(newsSpot[0]-1 == x[0] and newsSpot[1]+1 == x[1]):
                return False
        print("TRUE")
        return True


print(wallDict['V'])
print(wallDict['H'])
#validWall('z', (1, 3), 10, 10)
validWall('p', (3, 1), 10, 10)
