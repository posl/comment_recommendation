def solve():
    N,C = map(int,input().split())
    D = [list(map(int,input().split())) for _ in range(C)]
    c = [list(map(int,input().split())) for _ in range(N)]
    mod = [[0]*3 for _ in range(C)]
    for i in range(N):
        for j in range(N):
            mod[(i+j)%3][c[i][j]-1] += 1
    ans = 10**9
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i != j and j != k and k != i:
                    tmp = 0
                    for l in range(C):
                        tmp += mod[0][l]*D[l][i]
                        tmp += mod[1][l]*D[l][j]
                        tmp += mod[2][l]*D[l][k]
                    ans = min(ans,tmp)
    print(ans)
solve()
