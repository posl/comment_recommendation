def getPermutation(s, k):
    s = list(s)
    s.sort()
    return dfs(s, k, 0, len(s))
