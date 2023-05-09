def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    matchsticks = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [-1] * (N + 1)
    dp[0] = 0
    prev = [-1] * (N + 1)
    for i in range(N + 1):
        if dp[i] < 0:
            continue
        for j in range(M):
            if i + matchsticks[A[j] - 1] <= N:
                if dp[i + matchsticks[A[j] - 1]] < dp[i] * 10 + A[j]:
                    dp[i + matchsticks[A[j] - 1]] = dp[i] * 10 + A[j]
                    prev[i + matchsticks[A[j] - 1]] = A[j]
    ans = []
    i = N
    while i > 0:
        ans.append(prev[i])
        i -= matchsticks[prev[i] - 1]
    ans.reverse()
    print(''.join(map(str, ans)))
