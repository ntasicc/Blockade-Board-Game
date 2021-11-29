wallDict = {
    'V': [(4, 3), (0, 1), (2, 2)],
    'H': [(1, 4), (6, 2)],
    'numXv': 0,
    'numXh': 0,
    'numOv': 0,
    'numOh': 0,
}


def initialStateOfWalls(dictionary: dict, k: int):
    dictionary['numXh'] = dictionary['numOh'] = dictionary['numXv'] = dictionary['numOv'] = k


initialStateOfWalls(wallDict, 3)
