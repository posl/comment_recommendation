def dfs(now, pre):
    for next in edges[now]:
        if next == pre:
            continue
        counter[next] += counter[now]
        dfs(next, now)
N, Q = map(int, input().split())
edges = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
counter = [0] * N
for i in range(Q):
    p, x = map(int, input().split())
    counter[p-1] += x
dfs(0, -1)
print(*counter)

if __name__ == '__main__':
    dfs()