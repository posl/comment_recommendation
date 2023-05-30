def dfs(i, a, b, c):
    if i == N:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a, b, c) > 0 else 10**10
    ret0 = dfs(i+1, a, b, c)
    ret1 = dfs(i+1, a+l[i], b, c) + 10 if a > 0 else 10**10
    ret2 = dfs(i+1, a, b+l[i], c) + 10 if b > 0 else 10**10
    ret3 = dfs(i+1, a, b, c+l[i]) + 10 if c > 0 else 10**10
    ret4 = dfs(i+1, a, b, c) + (0 if l[i] == 1 else 1)
    ret5 = dfs(i+1, a, b, c) + (0 if l[i] == 2 else 1)
    return min(ret0, ret1, ret2, ret3, ret4, ret5)
N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))
