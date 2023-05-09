def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    #nCk
    def comb(n, k):
        if n < k or k < 0:
            return 0
        if k == 0:
            return 1
        if k == 1:
            return n
        if k == n:
            return 1
        if k > n - k:
            k = n - k
        return comb(n - 1, k - 1) + comb(n - 1, k)
    #nPk
    def perm(n, k):
        if n < k or k < 0:
            return 0
        if k == 0:
            return 1
        if k == 1:
            return n
        if k == n:
            return 1
        return n * perm(n - 1, k - 1)
    #nHk
    def hom(n, k):
        return comb(n + k - 1, k)
    print((pow(2, n, mod) - 1 - comb(n, a) - comb(n, b)) % mod)

if __name__ == '__main__':
    main()