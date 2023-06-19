def main():
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    def solve(n, p, q):
        def dfs(n, a, b, c):
            if n == 0:
                return b, c
            k = a.index(n)
            return dfs(n-1, a[:k]+a[k+1:], b*k+c, c+1)
        return abs(dfs(n, list(range(1, n+1)), 0, 0)[0] - dfs(n, list(range(1, n+1)), 0, 0)[1])
    print(solve(n, p, q))

if __name__ == '__main__':
    main()