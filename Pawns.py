pawnsDict = {
    'X': [],
    'O': [],
}


def initialStateOfPawns(dictionary: dict, X1: tuple, X2: tuple, O1: tuple, O2: tuple):
    dictionary['X'] = [X1, X2]
    dictionary['O'] = [O1, O2]


initialStateOfPawns(pawnsDict, (1, 2), (3, 4), (9, 10), (11, 11))
print(pawnsDict)
