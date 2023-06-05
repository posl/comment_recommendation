def main():
    n,x,y = map(int,input().split())
    tree = [[] for i in range(n+1)]
    for i in range(n-1):
        u,v = map(int,input().split())
        tree[u].append(v)
        tree[v].append(u)
    res = []
    def dfs(x,y):
        if x == y:
            res.append(x)
            return True
        for i in tree[x]:
            if dfs(i,y):
                res.append(x)
                return True
    dfs(x,y)
    res.reverse()
    print(*res)

if __name__ == '__main__':
    main()