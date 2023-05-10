def stones(K,X):
    result = []
    for i in range(X - K + 1, X + K):
        result.append(i)
    return result
