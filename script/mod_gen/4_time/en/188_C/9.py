def getSecondPlace(players):
    #print(players)
    if len(players) == 2:
        return players[0] if players[0] < players[1] else players[1]
    else:
        players = [max(players[i], players[len(players)-1-i]) for i in range(int(len(players)/2))]
        return getSecondPlace(players)
N = int(input())
A = list(map(int, input().split()))
print(A.index(getSecondPlace(A))+1)
