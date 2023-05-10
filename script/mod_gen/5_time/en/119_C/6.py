def main():
    n,a,b,c = map(int,input().split())
    l = [int(input()) for _ in range(n)]
    inf = 10**10
    def dfs(cur,a,b,c):
        if cur == n:
            if min(a,b,c) > 0:
                return abs(a - A) + abs(b - B) + abs(c - C) - 30
            else:
                return inf
        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
        ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
        ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0,a,b,c))

if __name__ == '__main__':
    main()