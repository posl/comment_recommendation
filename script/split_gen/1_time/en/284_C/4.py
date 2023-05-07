def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    adj = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    visited = [False] * N
    count = 0
    for i in range(N):
        if visited[i]:
            continue
        count += 1
        stack = [i]
        while stack:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            for w in adj[v]:
                if visited[w]:
                    continue
                stack.append(w)
    print(count)
