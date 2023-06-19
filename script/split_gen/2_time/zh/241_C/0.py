def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                S[i] = S[i][:j] + '1' + S[i][j+1:]
            else:
                S[i] = S[i][:j] + '0' + S[i][j+1:]
    for i in range(N):
        for j in range(N):
            if S[i][j] == '0':
                S[i] = S[i][:j] + '1' + S[i][j+1:]
                if check(S):
                    print('Yes')
                    return
                S[i] = S[i][:j] + '0' + S[i][j+1:]
    print('No')
