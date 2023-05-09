def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    C = [list(map(int, input().split())) for _ in range(N)]
    for k in range(C):
        for i in range(C):
            for j in range(C):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    A = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            A[(i + j) % 3][C[i][j] - 1] += 1
    ans = 10**10
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                ans = min(ans, D[i][j] * A[0][j] + D[j][k] * A[1][k] + D[k][i] * A[2][i])
    print(ans)
main()

if __name__ == '__main__':
    main()