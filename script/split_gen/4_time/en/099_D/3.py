def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    mod = [[0]*C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            mod[(i+j)%3][c[i][j]-1] += 1
    ans = 10**10
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += mod[0][l]*D[l][i] + mod[1][l]*D[l][j] + mod[2][l]*D[l][k]
                ans = min(ans, tmp)
    print(ans)
