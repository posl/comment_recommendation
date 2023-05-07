def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(n):
        ans += a[i] * a[i] * (n - 1)
        ans %= mod
    for i in range(n):
        ans -= a[i] * a[i]
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()