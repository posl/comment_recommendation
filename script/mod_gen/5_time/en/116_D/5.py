def problem():
    N, K = map(int, input().split())
    T = []
    D = []
    for i in range(N):
        t, d = map(int, input().split())
        T.append(t)
        D.append(d)
    #print(N, K)
    #print(T)
    #print(D)
    T2 = []
    D2 = []
    for i in range(K):
        t = T[i]
        d = D[i]
        T2.append(t)
        D2.append(d)
    #print(T2)
    #print(D2)
    S = 0
    for i in range(K):
        S += D2[i]
    #print(S)
    V = len(set(T2))
    #print(V)
    ans = S + V*V
    #print(ans)
    for i in range(K, N):
        t = T[i]
        d = D[i]
        if t in T2:
            continue
        for j in range(K):
            t2 = T2[j]
            d2 = D2[j]
            if d2 <= d:
                T2[j] = t
                D2[j] = d
                S = S - d2 + d
                V = len(set(T2))
                ans = max(ans, S + V*V)
                break
    print(ans)

if __name__ == '__main__':
    problem()