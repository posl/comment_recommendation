def buy_snuke(N, A, P, X):
    min_price = 1000000000
    for i in range(N):
        if X[i] > 0:
            if P[i] < min_price:
                min_price = P[i]
    return min_price

if __name__ == '__main__':
    buy_snuke()