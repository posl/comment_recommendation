def main():
    n,m = map(int,input().split())
    edge = [list(map(int,input().split())) for _ in range(m)]
    adj = [[] for _ in range(n+1)]
    for u,v in edge:
        adj[u].append(v)
        adj[v].append(u)
    ans = 0
    for u,v in edge:
        color = [0]*(n+1)
        color[u] = 1
        color[v] = 2
        q = [u,v]
        while q:
            p = q.pop()
            for i in adj[p]:
                if color[i] == 0:
                    color[i] = 3 - color[p]
                    q.append(i)
                elif color[i] == color[p]:
                    ans += 1
                    break
    print(ans)
