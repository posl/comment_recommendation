def getBlackStones(K, X):
    stones = []
    for i in range(X-K+1, X+K):
        stones.append(i)
    return stones
