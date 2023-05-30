def dfs(s, k):
    if k == 0:
        return int(s)
    else:
        return dfs(s + "0", k - 1) + dfs(s + "2", k - 1)
k = int(input())
print(dfs("2", k - 1))
