def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for a in A:
            if i - a >= 0 and dp[i - a] != -1:
                dp[i] = max(dp[i], dp[i - a] + 1)
    ans = []
    i = N
    while i > 0:
        for a in A:
            if i - a >= 0 and dp[i - a] == dp[i] - 1:
                ans.append(a)
                i -= a
                break
    print(''.join(map(str, ans)))

if __name__ == '__main__':
    main()