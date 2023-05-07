def dfs(n, m, a):
    if len(a) == n:
        print(' '.join(map(str, a)))
        return
    for i in range(1, m+1):
        if len(a) > 0 and a[-1] >= i:
            continue
        a.append(i)
        dfs(n, m, a)
        a.pop()

if __name__ == '__main__':
    dfs()