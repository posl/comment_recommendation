def solve():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    
    S2 = set(S)
    for i in range(N):
        if S[i][0] == '!':
            if S[i][1:] in S2:
                return S[i][1:]
        else:
            if '!'+S[i] in S2:
                return S[i]
    return 'satisfiable'
print(solve())
