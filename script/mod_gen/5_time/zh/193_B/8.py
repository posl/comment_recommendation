def getMinPrice(N, A, P, X):
    min_price = -1
    for i in range(N):
        if X[i] > 0:
            if min_price == -1:
                min_price = P[i]
            elif min_price > P[i]:
                min_price = P[i]
    return min_price

if __name__ == '__main__':
    getMinPrice()