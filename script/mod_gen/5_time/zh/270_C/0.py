def main():
    n,x,y = map(int,input().split())
    x-=1
    y-=1
    edge = [[] for _ in range(n)]
    for _ in range(n-1):
        u,v = map(int,input().split())
        u-=1
        v-=1
        edge[u].append(v)
        edge[v].append(u)
    parent = [0]*n
    parent[x] = x
    stack = [x]
    while stack:
        v = stack.pop()
        for u in edge[v]:
            if u == parent[v]:
                continue
            parent[u] = v
            stack.append(u)
    ans = []
    while y != x:
        ans.append(y)
        y = parent[y]
    ans.append(x)
    print(*[v+1 for v in reversed(ans)])

if __name__ == '__main__':
    main()