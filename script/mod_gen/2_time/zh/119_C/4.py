def dfs(i, a, b, c, mp):
    if i == n:
        return abs(a - A) + abs(b - B) + abs(c - C) + mp
    ret = dfs(i + 1, a, b, c, mp)
    ret = min(ret, dfs(i + 1, a + l[i], b, c, mp + (10 if a == 0 else 0)))
    ret = min(ret, dfs(i + 1, a, b + l[i], c, mp + (10 if b == 0 else 0)))
    ret = min(ret, dfs(i + 1, a, b, c + l[i], mp + (10 if c == 0 else 0)))
    return ret
n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
print(dfs(0, 0, 0, 0, 0))
