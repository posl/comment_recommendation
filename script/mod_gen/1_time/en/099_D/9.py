def main():
    N, C = map(int, input().split())
    D = [[int(i) for i in input().split()] for _ in range(C)]
    c = [[int(i) for i in input().split()] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            c[i][j] -= 1
    C = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            C[(i + j) % 3][c[i][j]] += 1
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
                    tmp += D[l][i] * C[0][l]
                    tmp += D[l][j] * C[1][l]
                    tmp += D[l][k] * C[2][l]
                ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()