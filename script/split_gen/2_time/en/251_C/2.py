def solve():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    d = {}
    for i in range(N-1, -1, -1):
        if S[i] not in d:
            d[S[i]] = T[i]
    print(N - len(d))
