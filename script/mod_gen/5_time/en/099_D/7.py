def solve():
    N,C = map(int,input().split())
    D = [list(map(int,input().split())) for i in range(C)]
    c = [list(map(int,input().split())) for i in range(N)]
    mod = [[0]*C for i in range(3)]
    for i in range(N):
        for j in range(N):
            mod[(i+j)%3][c[i][j]-1] += 1
    ans = 100000000
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i]*mod[0][l]
                    tmp += D[l][j]*mod[1][l]
                    tmp += D[l][k]*mod[2][l]
                ans = min(ans,tmp)
    print(ans)

if __name__ == '__main__':
    solve()