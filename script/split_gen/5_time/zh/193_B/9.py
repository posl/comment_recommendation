def findMinPrice(N, A, P, X):
    minPrice = -1
    for i in range(N):
        if X[i] > 0:
            if minPrice == -1:
                minPrice = P[i]
            elif minPrice > P[i]:
                minPrice = P[i]
    return minPrice
