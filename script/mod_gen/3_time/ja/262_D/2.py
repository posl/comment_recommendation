def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mod = 998244353
    ans = 0
    for i in range(n):
        ans += a[i] * pow(2, i, mod) * pow(2, n - i - 1, mod)
    print(ans % mod)

if __name__ == '__main__':
    main()