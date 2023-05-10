def dfs(now, prev):
    for i in edge[now]:
        if i == prev:
            continue
        counter[i] += counter[now]
        dfs(i, now)
N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
counter = [0 for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
for i in range(Q):
    p, x = map(int, input().split())
    counter[p-1] += x
dfs(0, -1)
for i in counter:
    print(i, end=" ")

if __name__ == '__main__':
    dfs()