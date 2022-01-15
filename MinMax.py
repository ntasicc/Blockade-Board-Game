from StateOfTheBoard import allValidStates


def checkValue(stanje):
    score = 0
    temp1 = ()
    temp2 = ()
    temp3 = ()
    temp4 = ()
    for i in range(0, 2):
        current_pos = stanje[1]['X'][i]
        end0 = stanje[1]['startO'][0]
        end1 = stanje[1]['startO'][1]

        if(current_pos > end0):
            temp1 = current_pos
            temp2 = end0
        else:
            temp2 = current_pos
            temp1 = end0

        if(current_pos > end1):
            temp3 = current_pos
            temp4 = end1
        else:
            temp4 = current_pos
            temp3 = end1

        allWalls = stanje[2]['V']
        allWalls.extend(stanje[2]['H'])
        for wall in allWalls:
            if(((wall[0]+1, wall[1]+1) >= temp1) and ((wall[0]+1, wall[1]+1) <= temp2) or ((wall[0]+1, wall[1]+1) >= temp3) and ((wall[0]+1, wall[1]+1) <= temp4)):
                score += 2

        distance0 = abs((current_pos[0] - end0[0]) +
                        (current_pos[1] - end0[1]))
        distance1 = abs((current_pos[0] - end1[0]) +
                        (current_pos[1] - end1[1]))
        score += min(distance0, distance1)

    for i in range(0, 2):
        current_pos = stanje[1]['O'][i]
        end0 = stanje[1]['startX'][0]
        end1 = stanje[1]['startX'][1]

        if(current_pos > end0):
            temp1 = current_pos
            temp2 = end0
        else:
            temp2 = current_pos
            temp1 = end0

        if(current_pos > end1):
            temp3 = current_pos
            temp4 = end1
        else:
            temp4 = current_pos
            temp3 = end1

        allWalls = stanje[2]['V']
        allWalls.extend(stanje[2]['H'])
        for wall in allWalls:
            if(((wall[0]+1, wall[1]+1) >= temp1) and ((wall[0]+1, wall[1]+1) <= temp2) or ((wall[0]+1, wall[1]+1) >= temp3) and ((wall[0]+1, wall[1]+1) <= temp4)):
                score -= 2

        distance0 = abs((current_pos[0] - end0[0]) +
                        (current_pos[1] - end0[1]))
        distance1 = abs((current_pos[0] - end1[0]) +
                        (current_pos[1] - end1[1]))
        score -= min(distance0, distance1)

    score = 0 - score
    return score


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


def minimax3(state, depth, maximizingPlayer, tableSizeN, tableSizeM, alpha, beta, potez=None):

    if depth == 3:
        return (potez, checkValue(state))

    igrac = "X" if maximizingPlayer else "O"
    all_states = allValidStates(
        state[0], state[1], state[2], igrac, 1, tableSizeN, tableSizeM)
    all_states.extend(allValidStates(
        state[0], state[1], state[2], igrac, 2, tableSizeN, tableSizeM))

    if maximizingPlayer:
        best = (("banana"), -1000)

        for new_state in all_states:

            val = minimax3(new_state, depth + 1,
                           False, tableSizeN, tableSizeM, alpha, beta, new_state if potez is None else potez)
            best = max(best, val, key=lambda x: x[1])
            alpha = max(alpha, best, key=lambda x: x[1])

            if beta[1] <= alpha[1]:
                break

        return best

    else:
        best = (("banana"), 1000)

        for new_state in all_states:

            val = minimax3(new_state, depth + 1,
                           True, tableSizeN, tableSizeM, alpha, beta, new_state if potez is None else potez)
            best = min(best, val, key=lambda x: x[1])
            beta = min(beta, best, key=lambda x: x[1])

            if beta[1] <= alpha[1]:
                break

        return best
