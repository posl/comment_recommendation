def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    dp = [0] * (sum(A) + 1)
    dp[0] = 1
    for i in range(N):
        for j in range(sum(A), A[i] - 1, -1):
            if dp[j - A[i]]:
                dp[j] = 1
    ans = 0
    for i in range(len(dp)):
        if dp[i] and i <= W:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()