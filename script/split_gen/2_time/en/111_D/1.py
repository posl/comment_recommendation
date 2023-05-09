def solve():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    if N == 1:
        print(1)
        print(1)
        print('R')
        return
    if N == 2:
        if X[0] == X[1] and Y[0] == Y[1]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            return
        if X[0] == X[1]:
            print(2)
            print(1, abs(Y[0] - Y[1]))
            print('U' if Y[0] < Y[1] else 'D')
            print('U' if Y[0] < Y[1] else 'D')
            return
        if Y[0] == Y[1]:
            print(2)
            print(1, abs(X[0] - X[1]))
            print('R' if X[0] < X[1] else 'L')
            print('R' if X[0] < X[1] else 'L')
            return
        print(3)
        print(abs(X[0] - X[1]), 1, abs(Y[0] - Y[1]))
        print('R' if X[0] < X[1] else 'L')
        print('U' if Y[0] < Y[1] else 'D')
        print('R' if X[0] < X[1] else 'L')
        return
    if N == 3:
        if X[0] == X[1] == X[2] and Y[0] == Y[1] == Y[2]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            return
        if X[0] == X[1] == X[2]:
            print(2)
            print(1, abs(Y[0] - Y[1]))
            print('U' if Y[0] < Y[1] else 'D')
            print('U' if Y[0] < Y[1] else 'D')
            return
