def dfs(i):
    global flag
    if i == n:
        flag = True
        return
    if not flag:
        if used[s[i]] == 0 and used[t[i]] == 0:
            used[s[i]] = 1
            used[t[i]] = 1
            dfs(i+1)
            used[s[i]] = 0
            used[t[i]] = 0
        if used[s[i]] == 1 and used[t[i]] == 0:
            used[t[i]] = 1
            dfs(i+1)
            used[t[i]] = 0
        if used[s[i]] == 0 and used[t[i]] == 1:
            used[s[i]] = 1
            dfs(i+1)
            used[s[i]] = 0

if __name__ == '__main__':
    dfs()