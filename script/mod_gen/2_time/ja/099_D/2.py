def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    mod = 3
    cnt = [[0]*C for _ in range(mod)]
    for i in range(N):
        for j in range(N):
            cnt[(i+j)%mod][c[i][j]-1] += 1
    ans = 10**9
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(mod):
                    tmp += D[i][l]*cnt[l][j]
                    tmp += D[j][l]*cnt[l][k]
                    tmp += D[k][l]*cnt[l][i]
                ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()