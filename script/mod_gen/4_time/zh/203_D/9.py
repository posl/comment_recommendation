def solve():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    def check(x):
        B = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(N):
            for j in range(N):
                B[i + 1][j + 1] = B[i + 1][j] + B[i][j + 1] - B[i][j]
                if A[i][j] > x:
                    B[i + 1][j + 1] += 1
        for i in range(N - K + 1):
            for j in range(N - K + 1):
                if B[i + K][j + K] - B[i][j + K] - B[i + K][j] + B[i][j] <= (K * K) // 2:
                    return True
        return False
    lb = -1
    ub = 10 ** 9 + 1
    while ub - lb > 1:
        mid = (lb + ub) // 2
        if check(mid):
            ub = mid
        else:
            lb = mid
    print(ub)

if __name__ == '__main__':
    solve()