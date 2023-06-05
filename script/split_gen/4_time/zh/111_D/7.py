def solve():
    N = int(input())
    X, Y = [0] * N, [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    if N == 1:
        print(0)
        print()
        print()
        return
    if N == 2:
        if X[0] == X[1] or Y[0] == Y[1]:
            print(0)
            print()
            print()
        else:
            print(-1)
        return
    for i in range(N):
        for j in range(i + 1, N):
            if X[i] == X[j] and Y[i] == Y[j]:
                print(-1)
                return
    ans = 100
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                x0, y0 = X[i], Y[i]
                x1, y1 = X[j], Y[j]
                x2, y2 = X[k], Y[k]
                if x0 == x1:
                    if x1 == x2:
                        continue
                    if y0 == y1:
                        continue
                    if y1 == y2:
                        continue
                    if x0 < x1 < x2 or x0 > x1 > x2:
                        continue
                    if y1 < y0 < y2 or y1 > y0 > y2:
                        continue
                    if abs(x1 - x2) + abs(y0 - y1) + abs(y1 - y2) <= ans:
                        ans = abs(x1 - x2) + abs(y0 - y1) + abs(y1 - y2)
                        m = 3
                        d = [abs(x1 - x2), abs(y0 - y1), abs(y1 - y2)]
                        w = ['R', 'U', 'D']
                elif y0 == y1:
                    if y1 == y2:
                        continue
                    if x0 == x1:
                        continue
                    if x1 == x2:
                        continue
                    if x1 < x0 < x2 or x1 > x0 > x2:
                        continue
                    if y0 < y1 < y2 or y0 >
