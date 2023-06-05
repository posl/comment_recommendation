def func():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        a, b = map(int, input().split())
        X.append(a)
        Y.append(b)
    print(X)
    print(Y)
    if N == 1:
        print(1)
        print(1)
        print('U')
        return
    if N == 2:
        if X[0] == X[1]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            return
        elif Y[0] == Y[1]:
            print(2)
            print(1, 1)
            print('UR')
            print('RU')
            return
        else:
            print(-1)
            return
    if N == 3:
        if X[0] == X[1] == X[2]:
            print(2)
            print(1, 1)
            print('RUU')
            print('URD')
            return
        elif Y[0] == Y[1] == Y[2]:
            print(2)
            print(1, 1)
            print('URR')
            print('RUL')
            return
        else:
            print(-1)
            return
    if N >= 4:
        if X[0] == X[1] == X[2] == X[3]:
            print(2)
            print(1, 1)
            print('RUUU')
            print('URDD')
            for i in range(4, N):
                if X[i] != X[0]:
                    print('R'*(i-3)+'U'+'R'*(N-1-i)+'D')
                    return
            return
        elif Y[0] == Y[1] == Y[2] == Y[3]:
            print(2)
            print(1, 1)
            print('URRR')
            print('RULL')
            for i in range(4, N):
                if Y[i] != Y[0]:
                    print('U'*(i-3)+'R'+'U'*(N-1-i)+'L')
                    return
            return
        else:
            print(-1)
            return
