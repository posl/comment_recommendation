def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    mod = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            mod[(i + j) % 3][c[i][j] - 1] += 1
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i] * mod[0][l]
                    tmp += D[l][j] * mod[1][l]
                    tmp += D[l][k] * mod[2][l]
                ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()