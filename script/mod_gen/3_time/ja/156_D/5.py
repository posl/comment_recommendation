def main():
    n, a, b = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = pow(2, n, mod) - 1
    ans -= comb(n, a, mod)
    ans -= comb(n, b, mod)
    ans %= mod
    print(ans)

if __name__ == '__main__':
    main()