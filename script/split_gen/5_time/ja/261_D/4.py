def solve(N, M, X, CY):
    ans = 0
    for i in range(1, N + 1):
        ans = max(ans, X[i - 1])
        for j in range(M):
            if i >= CY[j][0]:
                ans = max(ans, X[i - 1] + CY[j][1])
    return ans
N, M = map(int, input().split())
X = list(map(int, input().split()))
CY = [list(map(int, input().split())) for i in range(M)]
print(solve(N, M, X, CY))
