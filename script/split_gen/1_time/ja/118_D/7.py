def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    A = [str(i) for i in A]
    A = "".join(A)
    dp = [-float("inf")] * (N + 1)
    dp[0] = 0
    for i in range(N):
        for a in A:
            if i + len(a) <= N:
                dp[i + len(a)] = max(dp[i + len(a)], dp[i] * 10 + int(a))
    print(dp[N])
