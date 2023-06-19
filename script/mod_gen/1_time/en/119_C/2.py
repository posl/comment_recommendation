def dfs(i, a, b, c):
    if i == N:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a, b, c) > 0 else float('inf')
    res0 = dfs(i+1, a, b, c)
    res1 = dfs(i+1, a+l[i], b, c) + 10
    res2 = dfs(i+1, a, b+l[i], c) + 10
    res3 = dfs(i+1, a, b, c+l[i]) + 10
    return min(res0, res1, res2, res3)
N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))
