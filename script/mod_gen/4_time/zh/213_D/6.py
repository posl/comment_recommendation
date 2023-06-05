def dfs(i, p, g, ans):
    ans.append(i)
    for j in g[i]:
        if j != p:
            dfs(j, i, g, ans)
            ans.append(i)

if __name__ == '__main__':
    dfs()