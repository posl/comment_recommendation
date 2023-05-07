def solve():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    #print(S)
    #print(T)
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            if S[i] == S[j]:
                if T[i] == T[j]:
                    return False
    return True
