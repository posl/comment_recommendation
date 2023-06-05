def findSecondPlace(players):
    n = len(players)
    if n == 2:
        return players[0] if players[0] > players[1] else players[1]
    else:
        winners = []
        for i in range(0, n, 2):
            if players[i] > players[i+1]:
                winners.append(players[i])
            else:
                winners.append(players[i+1])
        return findSecondPlace(winners)

if __name__ == '__main__':
    findSecondPlace()