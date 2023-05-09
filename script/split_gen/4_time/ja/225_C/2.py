def solve():
    N,M = map(int,input().split())
    B = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            B[i][j] -= i*7+j+1
    if all(all(b==0 for b in row) for row in B):
        print('Yes')
    else:
        print('No')
