def dfs(i, a, b, c, mp):
    if i == n:
        if a != 0 and b != 0 and c != 0:
            return abs(a - A) + abs(b - B) + abs(c - C) + mp - 30
        else:
            return float('inf')
    ret0 = dfs(i + 1, a, b, c, mp)
    ret1 = dfs(i + 1, a + l[i], b, c, mp + 10)
    ret2 = dfs(i + 1, a, b + l[i], c, mp + 10)
    ret3 = dfs(i + 1, a, b, c + l[i], mp + 10)
    return min(ret0, ret1, ret2, ret3)
n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
print(dfs(0, 0, 0, 0, 0))
