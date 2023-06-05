def dfs(h, w, s, i, j, v):
    s[i][j] = '#'
    v += 1
    if i > 0 and s[i-1][j] == '.':
        v = dfs(h, w, s, i-1, j, v)
    if i < h-1 and s[i+1][j] == '.':
        v = dfs(h, w, s, i+1, j, v)
    if j > 0 and s[i][j-1] == '.':
        v = dfs(h, w, s, i, j-1, v)
    if j < w-1 and s[i][j+1] == '.':
        v = dfs(h, w, s, i, j+1, v)
    s[i][j] = '.'
    return v

if __name__ == '__main__':
    dfs()