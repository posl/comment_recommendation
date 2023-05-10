def dfs(v):
    global seen
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
seen = [False] * (n+1)
dfs(1)
for i in range(1,n+1):
    if not seen[i]:
        print('No')
        exit()
print('Yes')
for i in range(2,n+1):
    print(graph[i][0])

if __name__ == '__main__':
    dfs()