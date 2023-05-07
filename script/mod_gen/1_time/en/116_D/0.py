def main():
    N, K = map(int, input().split())
    T = []
    D = []
    for i in range(N):
        t, d = map(int, input().split())
        T.append(t)
        D.append(d)
    T = [t-1 for t in T]
    D = [(d, i) for i, d in enumerate(D)]
    D.sort(reverse=True)
    Kinds = set()
    S = 0
    for i in range(K):
        t = T[D[i][1]]
        d = D[i][0]
        Kinds.add(t)
        S += d
    if len(Kinds) == K:
        print(S + K*K)
    else:
        Kinds = list(Kinds)
        Kinds.sort()
        Score = [0]*(K+1)
        for i in range(K):
            Score[i+1] = Score[i] + D[i][0]
        Max = 0
        for i in range(K):
            n = len(Kinds)
            for j in range(n):
                if T[D[i][1]] == Kinds[j]:
                    break
            k = i - j
            s = Score[i+1] + Score[K] - Score[K-k] + (n+1)*(n+1)
            Max = max(Max, s)
        print(Max)

if __name__ == '__main__':
    main()