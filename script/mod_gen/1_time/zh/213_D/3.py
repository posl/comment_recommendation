def dfs(now, prev):
    global res
    res.append(now)
    for next in G[now]:
        if next != prev:
            dfs(next, now)
            res.append(now)
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
res = []
dfs(0, -1)
print(*[i+1 for i in res])

if __name__ == '__main__':
    dfs()