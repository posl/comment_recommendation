def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    cnt = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cnt[(i + j) % 3][c[i][j] - 1] += 1
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += cnt[0][l] * D[l][i]
                    tmp += cnt[1][l] * D[l][j]
                    tmp += cnt[2][l] * D[l][k]
                ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()