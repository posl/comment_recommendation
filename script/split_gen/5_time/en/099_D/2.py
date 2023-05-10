def solve():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    color = [[0]*C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            color[(i+j)%3][c[i][j]-1] += 1
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            if i==j: continue
            for k in range(C):
                if i==k or j==k: continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i]*color[0][l]
                    tmp += D[l][j]*color[1][l]
                    tmp += D[l][k]*color[2][l]
                ans = min(ans, tmp)
    print(ans)
