def solve():
    N = int(input())
    A = [list(map(int, input())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans, A[i][j] + A[i][(j + 1) % N] + A[i][(j + 2) % N] + A[(i + 1) % N][(j + 1) % N] + A[(i + 2) % N][(j + 2) % N])
    print(ans)
solve()

if __name__ == '__main__':
    solve()