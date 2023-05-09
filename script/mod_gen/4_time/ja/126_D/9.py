def dfs(node,par,dist,color):
    color[node] = dist % 2
    for i in edge[node]:
        if i == par:
            continue
        dfs(i,node,dist+1,color)
n = int(input())
edge = [[] for i in range(n)]
color = [0 for i in range(n)]
for i in range(n-1):
    u,v,w = map(int,input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)
dfs(0,-1,0,color)
for i in color:
    print(i)

if __name__ == '__main__':
    dfs()