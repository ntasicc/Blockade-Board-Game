from StateOfTheBoard import allValidStates


def checkValue(stanje):
    score = 0

    for i in range(0, 2):
        current_pos = (stanje[1]['X'][i][0] * 2 - 1,
                       stanje[1]['X'][i][1] * 2 - 1)
        end0 = (stanje[1]['startO'][0][0] * 2 - 1,
                stanje[1]['startO'][0][1] * 2 - 1)
        end1 = (stanje[1]['startO'][1][0] * 2 - 1,
                stanje[1]['startO'][1][1] * 2 - 1)

        distance0 = abs((current_pos[0] - end0[0]) +
                        (current_pos[1] - end0[1]))
        distance1 = abs((current_pos[0] - end1[0]) +
                        (current_pos[1] - end1[1]))
        score += min(distance0, distance1)

    for i in range(0, 2):
        current_pos = (stanje[1]['O'][i][0] * 2 - 1,
                       stanje[1]['O'][i][1] * 2 - 1)
        end0 = (stanje[1]['startX'][0][0] * 2 - 1,
                stanje[1]['startX'][0][1] * 2 - 1)
        end1 = (stanje[1]['startX'][1][0] * 2 - 1,
                stanje[1]['startX'][1][1] * 2 - 1)

        distance0 = abs((current_pos[0] - end0[0]) +
                        (current_pos[1] - end0[1]))
        distance1 = abs((current_pos[0] - end1[0]) +
                        (current_pos[1] - end1[1]))
        score -= min(distance0, distance1)

    return score


def max_value(tabla, depth, alpha, beta, pawnsDict, wallDict, tableSizeN, tableSizeM):
    if depth == 0:
        return (tabla, checkValue(pawnsDict), pawnsDict, wallDict)
    else:
        list_states = allValidStates(
            tabla, pawnsDict, wallDict, "X", 1, tableSizeN, tableSizeM)
        tempList = allValidStates(
            tabla, pawnsDict, wallDict, "X", 2, tableSizeN, tableSizeM)
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
        return (tabla, checkValue(pawnsDict), pawnsDict, wallDict)
    else:
        list_states = allValidStates(
            tabla, pawnsDict, wallDict, "O", 1, tableSizeN, tableSizeM)
        tempList = allValidStates(
            tabla, pawnsDict, wallDict, "O", 2, tableSizeN, tableSizeM)
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


def max_stanje(lsv, alpha, beta):
    alpha = max(max(lsv, key=lambda x: x[1]), alpha, key=lambda x: x[1])
    if alpha[1] >= beta[1]:
        return beta
    return alpha


def min_stanje(lsv, alpha, beta):
    beta = min(min(lsv, key=lambda x: x[1]), beta, key=lambda x: x[1])
    if beta[1] <= alpha[1]:
        return alpha
    return beta


def minimax2(stanje, dubina, moj_potez, tableSizeN, tableSizeM, alpha, beta, potez=None):
    igrac = "X" if moj_potez else "O"
    fja = max_stanje if moj_potez else min_stanje
    lp = allValidStates(
        stanje[0], stanje[1], stanje[2], igrac, 1, tableSizeN, tableSizeM)
    tempList = allValidStates(
        stanje[0], stanje[1], stanje[2], igrac, 2, tableSizeN, tableSizeM)
    lp.extend(tempList)
    if dubina == 0:
        return (potez, checkValue(stanje))

    if lp is None or len(lp) == 0:
        return (potez, checkValue(stanje))

    return fja(([minimax2(x, dubina - 1, not moj_potez, tableSizeN, tableSizeM, alpha, beta, x if potez is None else potez) for x in lp]), alpha, beta)
