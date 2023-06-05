def dfs(a, n, cnt):
    if a == n:
        return cnt
    elif a > n:
        return 999999
    else:
        return min(dfs(a*10, n, cnt+1), dfs(a*10+1, n, cnt+1))
a, n = map(int, input().split())
print(dfs(a, n, 1))
