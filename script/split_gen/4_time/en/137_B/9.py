def stones(K,X):
    start = X - K + 1
    end = X + K
    return [i for i in range(start, end)]
