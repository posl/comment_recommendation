def dfs(i, use3, use5, use7, n):
    if i > n:
        return 0
    ret = 1 if use3 and use5 and use7 else 0
    ret += dfs(i * 10 + 3, True, use5, use7, n)
    ret += dfs(i * 10 + 5, use3, True, use7, n)
    ret += dfs(i * 10 + 7, use3, use5, True, n)
    return ret
n = int(input())
print(dfs(0, False, False, False, n))
