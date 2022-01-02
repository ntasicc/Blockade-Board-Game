from Pawns import movePawn
from DrawBoard import DrawMove, ValidatePawnMove, DrawPawnMove
from Walls import placeWall, validWall, numOfWalls
from Pathfinding import astar
import copy


def changeState(tabla: list, pawnsPositions: dict, color: str, position: tuple, player: str, pawn: int, newSpot: tuple, wall: bool):
    tableForSimulation = copy.deepcopy(tabla)
    if(wall):
        DrawMove(tableForSimulation, pawnsPositions, color, position,
                 player, pawn, newSpot)
    else:
        DrawPawnMove(tableForSimulation, pawnsPositions, player,
                     pawn, newSpot)
    return tableForSimulation


def allValidStates(tabla: list, pawnsDict: dict, wallDict: dict, player: str, pawn: int, tableSizeN: int, tableSizeM: int):
    validTables = list()
    validPD = list()
    validWD = list()
    validSpots = list()
    coord: tuple = pawnsDict[player][pawn-1]
    spotsToCheck: list = [(coord[0]+2, coord[1]), (coord[0]-2, coord[1]), (coord[0], coord[1]+2), (coord[0], coord[1]-2),
                          (coord[0]+1, coord[1]+1), (coord[0]+1, coord[1]-1), (coord[0]-1, coord[1]+1), (coord[0]-1, coord[1]-1)]
    for s in spotsToCheck:
        spotAfterValidation = ValidatePawnMove(tabla,
                                               pawnsDict, player, pawn, s)
        if(spotAfterValidation):
            validSpots.append(spotAfterValidation)

    oldPawnsDict = copy.deepcopy(pawnsDict)
    oldWallDict = copy.deepcopy(wallDict)

    boje = ["p", "z"]
    for i in range(0, 2):
        bojaZida = boje[i]
        if(numOfWalls(wallDict, player, bojaZida)):
            for v in validSpots:
                for i in range(1, tableSizeN):
                    for j in range(1, tableSizeM):
                        if (validWall(player, bojaZida, (i, j), tableSizeN, tableSizeM)):
                            newTable = changeState(tabla, oldPawnsDict, bojaZida,
                                                   (i, j), player, pawn, v, True)
                            movePawn(oldPawnsDict, player, pawn,
                                     v)
                            placeWall(oldWallDict, player, bojaZida, (i, j))

                            if(astar(newTable, oldPawnsDict['X'][0], oldPawnsDict['startO'][0]) and astar(newTable, oldPawnsDict['X'][0], oldPawnsDict['startO'][1]) and astar(newTable, oldPawnsDict['X'][1], oldPawnsDict['startO'][0]) and astar(newTable, oldPawnsDict['X'][1], oldPawnsDict['startO'][1]) and astar(newTable, oldPawnsDict['O'][0], oldPawnsDict['startX'][0]) and astar(newTable, oldPawnsDict['O'][0], oldPawnsDict['startX'][1]) and astar(newTable, oldPawnsDict['O'][1], oldPawnsDict['startX'][0]) and astar(newTable, oldPawnsDict['O'][1], oldPawnsDict['startX'][1])):
                                validTables.append(newTable)
                                validPD.append(oldPawnsDict)
                                validWD.append(oldWallDict)

                            oldPawnsDict = copy.deepcopy(pawnsDict)
                            oldWallDict = copy.deepcopy(wallDict)
        else:
            for v in validSpots:
                newTable = changeState(tabla, oldPawnsDict, "",
                                       (0, 0), player, pawn, v, False)
                movePawn(oldPawnsDict, player, pawn,
                         v)
                validPD.append(oldPawnsDict)
                validTables.append(newTable)
                validWD.append(oldWallDict)
                oldPawnsDict = copy.deepcopy(pawnsDict)
    return [validTables, validPD, validWD]
