def main():
    n, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    MOD = 10 ** 9 + 7
    ans = pow(n, 2, MOD)
    ans -= (n - a + 1) ** 2
    ans -= (n - b + 1) ** 2
    ans += (n - a - b + 2) ** 2
    ans %= MOD
    ans *= pow(2, MOD - 2, MOD)
    print(ans)

if __name__ == '__main__':
    main()