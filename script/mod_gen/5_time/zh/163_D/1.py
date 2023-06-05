def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(k, n+2):
        min_sum = i * (i - 1) // 2
        max_sum = i * (2 * n - i + 1) // 2
        ans += max_sum - min_sum + 1
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()