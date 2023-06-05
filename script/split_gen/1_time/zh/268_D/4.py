def chokudai(S,T):
    if len(S) == 1:
        return S[0]
    else:
        for i in range(len(S)):
            for j in range(len(T)):
                if S[i] == T[j]:
                    return -1
        for i in range(len(S)):
            for j in range(len(S)):
                if i != j:
                    if S[i] == S[j]:
                        return -1
        for i in range(len(T)):
            for j in range(len(T)):
                if i != j:
                    if T[i] == T[j]:
                        return -1
        S1 = S[0]
        for i in range(1,len(S)):
            S1 = S1 + '_' + S[i]
        T1 = T[0]
        for i in range(1,len(T)):
            T1 = T1 + '_' + T[i]
        return S1 + '_' + T1
N,M = map(int,input().split())
S = []
T = []
for i in range(N):
    S.append(input())
for i in range(M):
    T.append(input())
print(chokudai(S,T))
