def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == '.':
                S[i] = S[i][:j] + '#' + S[i][j + 1:]
                for k in range(N):
                    for l in range(N):
                        if S[k][l] == '.':
                            S[k] = S[k][:l] + '#' + S[k][l + 1:]
                            for m in range(N - 5):
                                if S[i][m:m + 6] == '######':
                                    print('Yes')
                                    return
                                if S[m][j] == '#' and S[m + 1][j] == '#' and S[m + 2][j] == '#' and S[m + 3][j] == '#' and S[m + 4][j] == '#' and S[m + 5][j] == '#':
                                    print('Yes')
                                    return
                                if S[m][m + 5] == '#' and S[m + 1][m + 4] == '#' and S[m + 2][m + 3] == '#' and S[m + 3][m + 2] == '#' and S[m + 4][m + 1] == '#' and S[m + 5][m] == '#':
                                    print('Yes')
                                    return
                            S[k] = S[k][:l] + '.' + S[k][l + 1:]
                S[i] = S[i][:j] + '.' + S[i][j + 1:]
    print('No')
