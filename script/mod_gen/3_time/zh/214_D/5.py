def main():
    n = int(input())
    u = [0] * (n-1)
    v = [0] * (n-1)
    w = [0] * (n-1)
    for i in range(n-1):
        u[i], v[i], w[i] = map(int, input().split())
    #print(u)
    #print(v)
    #print(w)
    # 构建邻接表
    adj = [[] for _ in range(n+1)]
    for i in range(n-1):
        adj[u[i]].append((v[i], w[i]))
        adj[v[i]].append((u[i], w[i]))
    #print(adj)
    # 构建父节点
    parent = [-1] * (n+1)
    parent[1] = 0
    q = [1]
    while q:
        cur = q.pop(0)
        for next, _ in adj[cur]:
            if parent[next] == -1:
                parent[next] = cur
                q.append(next)
    #print(parent)
    # 计算每个节点的子节点的权重和
    child = [0] * (n+1)
    for i in range(2, n+1):
        child[parent[i]] += child[i] + 1
    #print(child)
    # 计算每个节点的子节点的权重和
    ans = 0
    for i in range(n-1):
        if parent[u[i]] == v[i]:
            ans += w[i] * (n - child[u[i]])
        else:
            ans += w[i] * (n - child[v[i]])
    print(ans)

if __name__ == '__main__':
    main()