wallDict = {
    'V': [(4, 3), (0, 1), (2, 2)],
    'H': [(1, 4), (6, 2)],
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


placeWall(wallDict, 'X', 'z', (5, 5))
placeWall(wallDict, 'O', 'p', (2, 0))
