def main():
    n, a, b = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = pow(2, n, mod) - 1
    a_c = 1
    b_c = 1
    for i in range(a):
        a_c *= (n - i)
        a_c %= mod
        a_c *= pow(i + 1, mod - 2, mod)
        a_c %= mod
    for i in range(b):
        b_c *= (n - i)
        b_c %= mod
        b_c *= pow(i + 1, mod - 2, mod)
        b_c %= mod
    ans -= a_c
    ans %= mod
    ans -= b_c
    ans %= mod
    print(ans)

if __name__ == '__main__':
    main()