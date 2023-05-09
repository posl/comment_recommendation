def path(x):
    if x == 0:
        return 0
    else:
        return path(parent[x]) ^ color[x]
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a-1].append([b-1,c])
    graph[b-1].append([a-1,c])
parent = [-1]*n
color = [0]*n
stack = [[0,-1,0]]
while stack:
    v,p,c = stack.pop()
    parent[v] = p
    color[v] = c
    for v2,c2 in graph[v]:
        if v2 == p:
            continue
        stack.append([v2,v,c2%2])
for i in range(n):
    print(path(i))
