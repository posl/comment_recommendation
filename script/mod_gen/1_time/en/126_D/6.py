def dfs(n, p, d, g):
    if n in g:
        for i in g[n]:
            if i[0] != p:
                d[i[0]] = d[n] + i[1]
                dfs(i[0], n, d, g)

if __name__ == '__main__':
    dfs()