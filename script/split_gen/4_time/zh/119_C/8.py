def dfs(i,a,b,c):
    if i == n:
        if a == 0 or b == 0 or c == 0:
            return float('inf')
        else:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
    ret0 = dfs(i + 1, a, b, c)
    ret1 = dfs(i + 1, a + l[i], b, c) + 10
    ret2 = dfs(i + 1, a, b + l[i], c) + 10
    ret3 = dfs(i + 1, a, b, c + l[i]) + 10
    return min(ret0, ret1, ret2, ret3)
n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
print(dfs(0, 0, 0, 0))
