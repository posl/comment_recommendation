def solve():
    N = int(input())
    X, Y = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    for m in range(1, 41):
        for d in range(1, 10**12+1):
            x, y = 0, 0
            for i in range(m):
                if abs(X[i]-x) + abs(Y[i]-y) > d:
                    break
                x = X[i]
                y = Y[i]
            else:
                print(m)
                print(*[d]*m)
                for i in range(N):
                    w = ""
                    x, y = 0, 0
                    for j in range(m):
                        if abs(X[i]-x) + abs(Y[i]-y) == d:
                            if X[i] > x:
                                w += "R"
                            elif X[i] < x:
                                w += "L"
                            elif Y[i] > y:
                                w += "U"
                            elif Y[i] < y:
                                w += "D"
                            else:
                                assert(False)
                            break
                        if X[i] > x:
                            x += d
                            w += "R"
                        elif X[i] < x:
                            x -= d
                            w += "L"
                        elif Y[i] > y:
                            y += d
                            w += "U"
                        elif Y[i] < y:
                            y -= d
                            w += "D"
                        else:
                            assert(False)
                    print(w)
                return
    print(-1)
solve()
