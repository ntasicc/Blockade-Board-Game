wallDict = {
    'V': [],
    'H': [],
    'numX': 0,
    'numO': 0,
}


def initialStateOfWalls(dictionary: dict, k: int):
    dictionary['numX'] = k
    dictionary['numO'] = k


initialStateOfWalls(wallDict, 3)
print(wallDict)
