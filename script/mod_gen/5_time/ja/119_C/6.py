def main():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    INF = 10 ** 9
    def dfs(cur, A, B, C):
        if cur == n:
            return abs(A - a) + abs(B - b) + abs(C - c) - 30 if min(A, B, C) > 0 else INF
        ret0 = dfs(cur + 1, A, B, C)
        ret1 = dfs(cur + 1, A + l[cur], B, C) + 10
        ret2 = dfs(cur + 1, A, B + l[cur], C) + 10
        ret3 = dfs(cur + 1, A, B, C + l[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))

if __name__ == '__main__':
    main()