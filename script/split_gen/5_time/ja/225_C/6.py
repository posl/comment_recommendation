def solve():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if B[i][j] != (i*7+j+1):
                print('No')
                return
    print('Yes')
