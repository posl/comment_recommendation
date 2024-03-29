def dfs(i, a, b, c):
    if i == N:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a, b, c) > 0 else 10**9
    ret0 = dfs(i+1, a, b, c)
    ret1 = dfs(i+1, a+l[i], b, c) + 10 if a else 10**9
    ret2 = dfs(i+1, a, b+l[i], c) + 10 if b else 10**9
    ret3 = dfs(i+1, a, b, c+l[i]) + 10 if c else 10**9
    return min(ret0, ret1, ret2, ret3)
N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))
