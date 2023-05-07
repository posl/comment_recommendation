def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == '.':
                S[i] = S[i][:j] + '#' + S[i][j + 1:]
                if check(S):
                    print('Yes')
                    return
                for k in range(j + 1, N):
                    if S[i][k] == '.':
                        S[i] = S[i][:k] + '#' + S[i][k + 1:]
                        if check(S):
                            print('Yes')
                            return
                        S[i] = S[i][:k] + '.' + S[i][k + 1:]
                S[i] = S[i][:j] + '.' + S[i][j + 1:]
    print('No')
