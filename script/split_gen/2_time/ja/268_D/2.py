def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(N):
        for j in range(i + 1, N):
            if S[i] in T or S[j] in T:
                continue
            for k in range(1, 17 - len(S[i]) - len(S[j]) + 1):
                X = S[i] + "_" * k + S[j]
                if X not in T:
                    print(X)
                    return
    print(-1)
