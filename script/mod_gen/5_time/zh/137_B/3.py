def getBlackStones(K, X):
    stones = []
    for i in range(X-K+1, X+K):
        stones.append(i)
    return stones

if __name__ == '__main__':
    getBlackStones()