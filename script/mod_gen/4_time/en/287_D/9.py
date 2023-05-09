def solve(S, T):
    N = len(S)
    M = len(T)
    #print(N, M)
    for i in range(0, M+1):
        S1 = S[0:i]
        S2 = S[i+M:]
        #print(S1, S2)
        if len(S1) != len(S2):
            return False
        for j in range(0, len(S1)):
            if S1[j] != '?' and S2[j] != '?' and S1[j] != S2[j]:
                return False
    return True

if __name__ == '__main__':
    solve()