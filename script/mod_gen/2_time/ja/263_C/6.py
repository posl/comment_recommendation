def dfs(l):
    if len(l) == n:
        print(*l)
        return
    for i in range(1,m+1):
        if len(l) == 0:
            dfs(l + [i])
        elif l[-1] < i:
            dfs(l + [i])
n,m = map(int,input().split())
dfs([])

if __name__ == '__main__':
    dfs()