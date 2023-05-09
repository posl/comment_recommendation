def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * m
    dp[0] = 1
    for i in range(n):
        dp_ = [0] * m
        for j in range(m):
            if dp[j] == 1:
                dp_[j] = 1
                dp_[(j + a[i]) % m] = 1
        dp = dp_
    ans = sum([i for i in range(m) if dp[i] == 1])
    print(ans)

if __name__ == '__main__':
    main()