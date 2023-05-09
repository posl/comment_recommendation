def main():
    A, B, K = map(int, input().split())
    def comb(n, r):
        if n == r or r == 0:
            return 1
        else:
            return comb(n-1, r) + comb(n-1, r-1)
    def dfs(s, a, b, k):
        if a == 0 or b == 0:
            return s + 'a' * a + 'b' * b
        elif k <= comb(a + b - 1, b):
            return dfs(s + 'a', a - 1, b, k)
        else:
            return dfs(s + 'b', a, b - 1, k - comb(a + b - 1, b))
    print(dfs('', A, B, K))

if __name__ == '__main__':
    main()