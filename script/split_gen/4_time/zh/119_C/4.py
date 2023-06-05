def dfs(depth, a, b, c):
    if depth == n:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else 10 ** 9
    ret0 = dfs(depth + 1, a, b, c)
    ret1 = dfs(depth + 1, a + l[depth], b, c) + 10
    ret2 = dfs(depth + 1, a, b + l[depth], c) + 10
    ret3 = dfs(depth + 1, a, b, c + l[depth]) + 10
    return min(ret0, ret1, ret2, ret3)
n, A, B, C = map(int, input().split())
l = [int(input()) for i in range(n)]
print(dfs(0, 0, 0, 0))
