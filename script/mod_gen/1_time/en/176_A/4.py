def takoyaki():
    N, X, T = map(int, input().split())
    print((N + X - 1) // X * T)
takoyaki()

if __name__ == '__main__':
    takoyaki()