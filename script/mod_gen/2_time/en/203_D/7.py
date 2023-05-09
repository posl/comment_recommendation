def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    def is_ok(x):
        B = [[1 if A[i][j] > x else 0 for j in range(N)] for i in range(N)]
        C = [[0 for j in range(N+1)] for i in range(N+1)]
        for i in range(N):
            for j in range(N):
                C[i+1][j+1] = C[i+1][j] + C[i][j+1] - C[i][j] + B[i][j]
        for i in range(N-K+1):
            for j in range(N-K+1):
                if C[i+K][j+K] - C[i][j+K] - C[i+K][j] + C[i][j] <= K**2//2:
                    return True
        return False
    ok = 10**9
    ng = -1
    while ok - ng > 1:
        mid = (ok+ng)//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    print(ok)

if __name__ == '__main__':
    main()