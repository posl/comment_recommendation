def solve():
    N, M = list(map(int, input().split()))
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(2 ** N):
        x = []
        for j in range(N):
            if (i >> j) & 1:
                x.append(S[j])
            else:
                x.append("_" * len(S[j]))
        X = "".join(x)
        if 3 <= len(X) <= 16 and X not in T:
            print(X)
            return
    print(-1)
