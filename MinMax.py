from StateOfTheBoard import allValidStates


def checkValue(tabla):
    return


def max_value(tabla, depth, alpha, beta, pawnsDict, wallDict, tableSizeN, tableSizeM):
    if depth == 0:
        return (tabla, checkValue(tabla))
    else:
        list_states = allValidStates(
            tabla, pawnsDict, wallDict, "X", 1, tableSizeN, tableSizeN)
        list_states.append(allValidStates(
            tabla, pawnsDict, wallDict, "X", 2, tableSizeN, tableSizeN))
        for s in list_states:
            alpha = max(alpha, min_value(tabla, depth-1, alpha, beta,
                                         pawnsDict, wallDict, tableSizeN, tableSizeM), key=lambda x: x[1])
            if alpha[1] >= beta[1]:
                return beta
    return alpha


def min_value(tabla, depth, alpha, beta, pawnsDict, wallDict, tableSizeN, tableSizeM):
    if depth == 0:
        return (tabla, checkValue(tabla))
    else:
        list_states = allValidStates(
            tabla, pawnsDict, wallDict, "O", 1, tableSizeN, tableSizeN)
        list_states.append(allValidStates(
            tabla, pawnsDict, wallDict, "O", 2, tableSizeN, tableSizeN))
        for s in list_states:
            beta = max(beta, max_value(tabla, depth-1, alpha, beta,
                                       pawnsDict, wallDict, tableSizeN, tableSizeM), key=lambda x: x[1])
            if beta[1] <= alpha[1]:
                return alpha
    return beta


def minimax(tabla, depth, alpha, beta, pawnsDict, wallDict, tableSizeN, tableSizeM):
    return min_value(tabla, depth, alpha, beta, pawnsDict, wallDict, tableSizeN, tableSizeM)
