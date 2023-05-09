def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(k, n + 2):
        a = i * (n - i + 1) + 1
        b = i * (i - 1) // 2
        ans += a - b
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()