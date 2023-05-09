def main():
    import sys
    input = sys.stdin.readline
    from collections import Counter
    from itertools import accumulate
    n, a, b = map(int, input().split())
    MOD = 10**9 + 7
    def cmb(n, r, mod):
        if r > n - r:
            r = n - r
        if r == 0:
            return 1
        if r == 1:
            return n
        numer = reduce(lambda x, y: x * y % mod, range(n, n - r, -1))
        denom = reduce(lambda x, y: x * y % mod, range(1, r + 1))
        return numer * pow(denom, mod - 2, mod) % mod
    def cmb2(n, r, mod):
        numer = reduce(lambda x, y: x * y % mod, range(n, n - r, -1))
        denom = reduce(lambda x, y: x * y % mod, range(1, r + 1))
        return numer * pow(denom, mod - 2, mod) % mod
    def cmb3(n, r, mod):
        numer = reduce(lambda x, y: x * y % mod, range(n, n - r, -1))
        denom = reduce(lambda x, y: x * y % mod, range(1, r + 1))
        return numer * pow(denom, mod - 2, mod) % mod
    def cmb4(n, r, mod):
        numer = reduce(lambda x, y: x * y % mod, range(n, n - r, -1))
        denom = reduce(lambda x, y: x * y % mod, range(1, r + 1))
        return numer * pow(denom, mod - 2, mod) % mod
    def cmb5(n, r, mod):
        numer = reduce(lambda x, y: x * y % mod, range(n, n - r, -1))
        denom = reduce(lambda x, y: x * y % mod, range(1, r + 1))
        return numer * pow(denom, mod - 2, mod) % mod
    def cmb6(n, r, mod):
        numer = reduce(lambda x, y: x * y %

if __name__ == '__main__':
    main()