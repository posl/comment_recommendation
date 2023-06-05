def main():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    ans = 10**9
    def dfs(cur, mp, a, b, c):
        if cur == n:
            if min(a, b, c) > 0:
                return mp + abs(a - A) + abs(b - B) + abs(c - C) - 30
            else:
                return 10**9
        ret0 = dfs(cur + 1, mp, a, b, c)
        ret1 = dfs(cur + 1, mp + 10, a + l[cur], b, c)
        ret2 = dfs(cur + 1, mp + 10, a, b + l[cur], c)
        ret3 = dfs(cur + 1, mp + 10, a, b, c + l[cur])
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, a, b, c))

if __name__ == '__main__':
    main()