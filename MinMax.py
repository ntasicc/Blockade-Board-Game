from StateOfTheBoard import allValidStates


def checkValue(pawnsDict):
    score = 0

    for i in range(0, 2):
        current_pos = (pawnsDict['X'][i][0] * 2 - 1,
                       pawnsDict['X'][i][1] * 2 - 1)
        end0 = (pawnsDict['startO'][0][0] * 2 - 1,
                pawnsDict['startO'][0][1] * 2 - 1)
        end1 = (pawnsDict['startO'][1][0] * 2 - 1,
                pawnsDict['startO'][1][1] * 2 - 1)

        distance0 = abs((current_pos[0] - end0[0]) +
                        (current_pos[1] - end0[1]))
        distance1 = abs((current_pos[0] - end1[0]) +
                        (current_pos[1] - end1[1]))
        score += min(distance0, distance1)

    for i in range(0, 2):
        current_pos = (pawnsDict['O'][i][0] * 2 - 1,
                       pawnsDict['O'][i][1] * 2 - 1)
        end0 = (pawnsDict['startX'][0][0] * 2 - 1,
                pawnsDict['startX'][0][1] * 2 - 1)
        end1 = (pawnsDict['startX'][1][0] * 2 - 1,
                pawnsDict['startX'][1][1] * 2 - 1)

        distance0 = abs((current_pos[0] - end0[0]) +
                        (current_pos[1] - end0[1]))
        distance1 = abs((current_pos[0] - end1[0]) +
                        (current_pos[1] - end1[1]))
        score -= min(distance0, distance1)

    return score


def max_value(tabla, depth, alpha, beta, pawnsDict, wallDict, tableSizeN, tableSizeM):
    if depth == 0:
        return (tabla, checkValue(pawnsDict))
    else:
        list_states = allValidStates(
            tabla, pawnsDict, wallDict, "X", 1, tableSizeN, tableSizeN)
        tempList = allValidStates(
            tabla, pawnsDict, wallDict, "X", 2, tableSizeN, tableSizeN)
        list_states[0].extend(tempList[0])
        list_states[1].extend(tempList[1])
        list_states[2].extend(tempList[2])

        for s in list_states[0]:
            index = list_states[0].index(s)
            alpha = max(alpha, min_value(s, depth-1, alpha, beta,
                                         list_states[1][index], list_states[2][index], tableSizeN, tableSizeM), key=lambda x: x[1])
            if alpha[1] >= beta[1]:
                return beta

    return alpha


def min_value(tabla, depth, alpha, beta, pawnsDict, wallDict, tableSizeN, tableSizeM):
    if depth == 0:
        return (tabla, checkValue(pawnsDict))
    else:
        list_states = allValidStates(
            tabla, pawnsDict, wallDict, "O", 1, tableSizeN, tableSizeN)
        tempList = allValidStates(
            tabla, pawnsDict, wallDict, "O", 2, tableSizeN, tableSizeN)
        list_states[0].extend(tempList[0])
        list_states[1].extend(tempList[1])
        list_states[2].extend(tempList[2])
        for s in list_states[0]:
            index = list_states[0].index(s)
            beta = min(beta, max_value(s, depth-1, alpha, beta,
                                       list_states[1][index], list_states[2][index], tableSizeN, tableSizeM), key=lambda x: x[1])
            if beta[1] <= alpha[1]:
                return alpha
    return beta


def minimax(tabla, depth, alpha, beta, pawnsDict, wallDict, tableSizeN, tableSizeM):
    return min_value(tabla, depth, alpha, beta, pawnsDict, wallDict, tableSizeN, tableSizeM)
