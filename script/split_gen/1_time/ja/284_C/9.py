def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print("---------------")
    if M == 0:
        print(N)
        return
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    #print(G)
    #print("---------------")
    visited = [False] * N
    #print(visited)
    #print("---------------")
    ans = 0
    for i in range(N):
        if visited[i]:
            continue
        ans += 1
        q = [i]
        while q:
            now = q.pop()
            visited[now] = True
            for next in G[now]:
                if visited[next]:
                    continue
                q.append(next)
    print(ans)
