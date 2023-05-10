def solve():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        for j in range(N):
            if S[i][j] == '.':
                S[i] = S[i][:j] + '#' + S[i][j+1:]
                if check(S):
                    print('Yes')
                    return
                S[i] = S[i][:j] + '.' + S[i][j+1:]
    print('No')
