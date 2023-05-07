def dfs(cand, path, n):
    if len(path) == n:
        print(*path)
        return
    for i in range(len(cand)):
        dfs(cand[i+1:], path+[cand[i]], n)
n, m = map(int, input().split())
dfs(list(range(1, m+1)), [], n)
