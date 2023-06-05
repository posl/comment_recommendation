def main():
    n,m,k = map(int, input().split())
    # 建立邻接表
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # 建立阻隔表
    block = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(k):
        c,d = map(int, input().split())
        block[c-1][d-1] = True
        block[d-1][c-1] = True
    # 深度优先搜索
    ans = [0 for _ in range(n)]
    for i in range(n):
        visited = [False for _ in range(n)]
        visited[i] = True
        stack = [i]
        while stack:
            s = stack.pop()
            for j in adj[s]:
                if visited[j]: continue
                if block[s][j]: continue
                ans[i] += 1
                visited[j] = True
                stack.append(j)
    print(*ans)
    return
