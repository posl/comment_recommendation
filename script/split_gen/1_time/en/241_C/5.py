def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == '.':
                S[i][j] = '#'
                if check(S):
                    print('Yes')
                    exit()
                S[i][j] = '.'
    print('No')
