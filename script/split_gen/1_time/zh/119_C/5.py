def solve():
    N, A, B, C = map(int, input().split())
    l = sorted([int(input()) for _ in range(N)], reverse=True)
    INF = float('inf')
    def dfs(i, a, b, c):
        if i == N:
            return abs(A-a) + abs(B-b) + abs(C-c) - 30 if min(a, b, c) > 0 else INF
        ret0 = dfs(i+1, a, b, c)
        ret1 = dfs(i+1, a+l[i], b, c) + 10
        ret2 = dfs(i+1, a, b+l[i], c) + 10
        ret3 = dfs(i+1, a, b, c+l[i]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))
solve()
