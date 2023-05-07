def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    dp = [0] * (A[-1]+1)
    for i in range(N):
        dp[A[i]] += 1
    ans = 0
    for i in range(1, A[-1]+1):
        cnt = 0
        for j in range(i, A[-1]+1, i):
            cnt += dp[j]
        if cnt >= 2:
            ans += cnt * (cnt-1) // 2
    print(ans)

if __name__ == '__main__':
    main()