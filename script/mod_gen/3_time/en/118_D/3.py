def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        if dp[i] == -1:
            continue
        for j in range(M):
            if i + match[A[j]] <= N:
                dp[i + match[A[j]]] = max(dp[i + match[A[j]]], dp[i] * 10 + A[j])
    print(dp[N])
match = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
solve()

if __name__ == '__main__':
    solve()