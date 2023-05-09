def solve():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    if N == 1:
        print(2)
        print(1, 1)
        print("RU")
        print("UR")
        return
    if N == 2:
        if X[0] == X[1] and Y[0] == Y[1]:
            print(2)
            print(1, 1)
            print("RU")
            print("UR")
            return
        else:
            print(-1)
            return
    # N >= 3
    m = 40
    d = [1] * m
    for i in range(1, m):
        d[i] = d[i-1] * 2
    w = [""] * N
    for i in range(N):
        if X[i] < 0:
            w[i] += "L" * abs(X[i])
        else:
            w[i] += "R" * abs(X[i])
        if Y[i] < 0:
            w[i] += "D" * abs(Y[i])
        else:
            w[i] += "U" * abs(Y[i])
    print(m)
    print(*d)
    for i in range(N):
        print(w[i])
