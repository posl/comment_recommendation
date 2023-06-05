def solve():
    N,M = map(int,input().split())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())
    S.sort(key=len)
    T.sort(key=len)
    S.reverse()
    T.reverse()
    #print(S)
    #print(T)
    for i in range(M):
        for j in range(M):
            if i==j:
                continue
            if T[i] in T[j]:
                T[j] = T[j].replace(T[i],'')
    #print(T)
    for i in range(N):
        for j in range(M):
            if S[i] in T[j]:
                T[j] = T[j].replace(S[i],'')
    #print(T)
    for i in range(M):
        if T[i]!='':
            print(T[i])
            return
    print(-1)
    return
