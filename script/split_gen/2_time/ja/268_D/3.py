def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(3, 17):
        for j in range(1 << (i - 1)):
            X = ''
            for k in range(N):
                if k > 0:
                    for l in range(i - 1):
                        if j >> l & 1:
                            X += '_'
                X += S[k]
            if len(X) != i:
                continue
            if X in T:
                continue
            print(X)
            return
    print(-1)
