def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    INF = 10**9
    # DFS
    def dfs(cur, a, b, c):
        if cur == N:
            if min(a, b, c) > 0:
                return abs(a - A) + abs(b - B) + abs(c - C) - 30
            else:
                return INF
        # 使わない場合
        ret0 = dfs(cur + 1, a, b, c)
        # Aに使う場合
        ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
        # Bに使う場合
        ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
        # Cに使う場合
        ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))

if __name__ == '__main__':
    main()