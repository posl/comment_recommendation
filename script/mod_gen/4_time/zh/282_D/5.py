def solve(n, m, u, v):
    # 从1开始，所以需要n+1
    color = [0] * (n + 1)
    # 从1开始，所以需要n+1
    g = [[] for _ in range(n + 1)]
    for i in range(m):
        g[u[i]].append(v[i])
        g[v[i]].append(u[i])
    # print(g)
    ans = 0
    for i in range(1, n + 1):
        # 如果当前节点没有被染色
        if color[i] == 0:
            # 从当前节点开始染色
            ans += 1
            q = [i]
            color[i] = 1
            while len(q) != 0:
                cur = q.pop()
                # 遍历当前节点的所有邻接边
                for j in g[cur]:
                    # 如果当前节点和邻接边的颜色相同，返回False
                    if color[j] == color[cur]:
                        return 0
                    # 如果邻接边没有被染色，那么染成和当前节点不同的颜色
                    if color[j] == 0:
                        color[j] = -color[cur]
                        q.append(j)
    return ans

if __name__ == '__main__':
    solve()