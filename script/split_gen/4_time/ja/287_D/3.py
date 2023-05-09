def solve():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    for i in range(N-M+1):
        for j in range(M):
            if S[i+j] != T[j] and S[i+j] != '?':
                break
        else:
            print('Yes')
            return
    print('No')
