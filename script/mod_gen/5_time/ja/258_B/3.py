def main():
    N = int(input())
    A = [list(map(int, input())) for _ in range(N)]
    ans = -1
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                continue
            ans = max(ans, A[i][j] * A[(i + 1) % N][j] * A[(i + 2) % N][j] * A[(i + 3) % N][j])
            ans = max(ans, A[i][j] * A[i][(j + 1) % N] * A[i][(j + 2) % N] * A[i][(j + 3) % N])
            ans = max(ans, A[i][j] * A[(i + 1) % N][(j + 1) % N] * A[(i + 2) % N][(j + 2) % N] * A[(i + 3) % N][(j + 3) % N])
            ans = max(ans, A[i][j] * A[(i + 1) % N][(j - 1) % N] * A[(i + 2) % N][(j - 2) % N] * A[(i + 3) % N][(j - 3) % N])
    print(ans)

if __name__ == '__main__':
    main()