def dfs(n, m, pre, ans):
    if n == 0:
        print(*ans)
        return
    for i in range(pre + 1, m + 1):
        dfs(n - 1, m, i, ans + [i])

if __name__ == '__main__':
    dfs()