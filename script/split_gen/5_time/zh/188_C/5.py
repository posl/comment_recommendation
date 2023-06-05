def findSecondPlace(n, scores):
    players = [i for i in range(1, 2 ** n + 1)]
    players.sort(key=lambda x: scores[x - 1])
    players.reverse()
    return players[1]
