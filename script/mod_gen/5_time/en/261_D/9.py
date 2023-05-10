def get_max_coin(N, M, X, C, Y):
    max_coin = 0
    for i in range(N):
        coin = X[i]
        for j in range(M):
            if i + 1 == C[j]:
                coin += Y[j]
        if max_coin < coin:
            max_coin = coin
    return max_coin

if __name__ == '__main__':
    get_max_coin()