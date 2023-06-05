def dfs(a, b, c, mp, l, n):
    if n == N:
        if a == 0 or b == 0 or c == 0:
            return 10**9
        else:
            return mp + abs(a - A) + abs(b - B) + abs(c - C) - 30
    ret0 = dfs(a, b, c, mp, l, n + 1)
    ret1 = dfs(a + l[n], b, c, mp + 10, l, n + 1)
    ret2 = dfs(a, b + l[n], c, mp + 10, l, n + 1)
    ret3 = dfs(a, b, c + l[n], mp + 10, l, n + 1)
    return min(ret0, ret1, ret2, ret3)
N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0, l, 0))
