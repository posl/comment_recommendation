def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    visited = [False] * N
    ans = 0
    for i in range(N):
        if visited[i]:
            continue
        ans += 1
        stack = [i]
        while stack:
            j = stack.pop()
            if visited[j]:
                continue
            visited[j] = True
            for k in G[j]:
                if visited[k]:
                    continue
                stack.append(k)
    print(ans)
