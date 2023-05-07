def main():
    n, a, b = map(int, input().split())
    mod = 10**9+7
    ans = pow(2, n, mod) - 1
    for i in range(a, b+1):
        ans -= comb(n, i, mod)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()