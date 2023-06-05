def main():
    n,q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    px = [list(map(int, input().split())) for _ in range(q)]
    #print("n,q:",n,q)
    #print("ab:",ab)
    #print("px:",px)
    #构建树，用邻接表表示
    #根据ab构建邻接表
    adj = [[] for _ in range(n+1)]
    for i in range(n-1):
        a,b = ab[i]
        adj[a].append(b)
        adj[b].append(a)
    #print("adj:",adj)
    #构建树，用邻接表表示
    #根据ab构建邻接表
    adj = [[] for _ in range(n+1)]
    for i in range(n-1):
        a,b = ab[i]
        adj[a].append(b)
        adj[b].append(a)
    #print("adj:",adj)
    #计算每个节点的子节点数
    #计算每个节点的子节点数
    #print("adj:",adj)
    #print("px:",px)
    #print("n,q:",n,q)
    #print("ab:",ab)
    #print("px:",px)
    #构建树，用邻接表表示
    #根据ab构建邻接表
    adj = [[] for _ in range(n+1)]
    for i in range(n-1):
        a,b = ab[i]
        adj[a].append(b)
        adj[b].append(a)
    #print("adj:",adj)
    #计算每个节点的子节点数
    def dfs(x,par):
        for y in adj[x]:
            if y == par:
                continue
            dfs(y,x)
            c[x] += c[y]
    c = [0]*(n+1)
    for i in range(q):
        p,x = px[i]
        c[p] += x
    #print("c:",c)
    dfs(1,0)
    print(" ".join(map(str,c[1:])))
