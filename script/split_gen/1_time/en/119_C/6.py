def dfs(i, a, b, c):
    if i == N: return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else 10**9
    res0 = dfs(i + 1, a, b, c)
    res1 = dfs(i + 1, a + L[i], b, c) + 10 if a else 10**9
    res2 = dfs(i + 1, a, b + L[i], c) + 10 if b else 10**9
    res3 = dfs(i + 1, a, b, c + L[i]) + 10 if c else 10**9
    return min(res0, res1, res2, res3)
N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))
