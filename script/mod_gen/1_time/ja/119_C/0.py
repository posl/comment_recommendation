def dfs(i, a, b, c):
    if i == n:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else float('inf')
    ret0 = dfs(i + 1, a, b, c)
    ret1 = dfs(i + 1, a + L[i], b, c) + 10
    ret2 = dfs(i + 1, a, b + L[i], c) + 10
    ret3 = dfs(i + 1, a, b, c + L[i]) + 10
    return min(ret0, ret1, ret2, ret3)
n, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(n)]
print(dfs(0, 0, 0, 0))
