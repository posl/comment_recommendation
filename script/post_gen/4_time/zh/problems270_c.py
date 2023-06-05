Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n,x,y = map(int,input().split())
    uv = []
    for i in range(n-1):
        uv.append(list(map(int,input().split())))
    #print(uv)
    path = [x]
    for i in range(n-1):
        if uv[i][0] == path[-1]:
            path.append(uv[i][1])
        elif uv[i][1] == path[-1]:
            path.append(uv[i][0])
    #print(path)
    for i in range(len(path)):
        if path[i] == y:
            print(*path[:i+1])
            break

=======
Suggestion 3

def main():
    n,x,y=map(int,input().split())
    x,y=x-1,y-1
    tree=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=map(int,input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    #print(tree)
    #print(x,y)
    #print(tree[x])
    #print(tree[y])
    #print(set(tree[x])&set(tree[y]))
    #print(set(tree[x])|set(tree[y]))
    #print(set(tree[x])^set(tree[y]))
    #print(set(tree[x])^set(tree[y])&set(tree[x]))
    #print(set(tree[x])^set(tree[y])&set(tree[y]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x])^set(tree[y]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x])^set(tree[y])&set(tree[x]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x])^set(tree[y])&set(tree[x])|set(tree[x])^set(tree[y]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x])^set(tree[y])&set(tree[x])|set(tree[x])^set(tree[y])&set(tree[x]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x])^set(tree[y])&set(tree[x])|set(tree[x])^set(tree[y])&set(tree[x])|set(tree[x]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x])^set(tree[y])&set(tree[x])|set(tree[x])^set(tree[y])&set(tree[x])|set(tree[x])^set(tree[y])&set(tree[y]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x])^set(tree[y])&set(tree[x])|set(tree[x])^set(tree[y])&set(tree[x])|set

=======
Suggestion 4

def dfs(i,p):
    global d
    d[i]=p
    for j in g[i]:
        if j==p: continue
        dfs(j,i)

n,x,y=map(int,input().split())
x-=1
y-=1
g=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
d=[-1]*n
dfs(x,-1)
ans=[]
while y!=-1:
    ans.append(y)
    y=d[y]
for i in reversed(ans):
    print(i+1,end=" ")
print()

=======
Suggestion 5

def main():
    n,x,y = map(int,input().split())
    u = [0]*(n-1)
    v = [0]*(n-1)
    for i in range(n-1):
        u[i],v[i] = map(int,input().split())
    # print(n,x,y,u,v)
    # print(type(n),type(x),type(y),type(u),type(v))
    # print(len(u),len(v))
    # print(u)
    # print(v)
    # print(u[0])
    # print(v[0])
    # print(u[1])
    # print(v[1])
    # print(u[2])
    # print(v[2])
    # print(u[3])
    # print(v[3])
    # print(u[4])
    # print(v[4])
    # print(u[5])
    # print(v[5])
    # print(u[6])
    # print(v[6])
    # print(u[7])
    # print(v[7])
    # print(u[8])
    # print(v[8])
    # print(u[9])
    # print(v[9])
    # print(u[10])
    # print(v[10])
    # print(u[11])
    # print(v[11])
    # print(u[12])
    # print(v[12])
    # print(u[13])
    # print(v[13])
    # print(u[14])
    # print(v[14])
    # print(u[15])
    # print(v[15])
    # print(u[16])
    # print(v[16])
    # print(u[17])
    # print(v[17])
    # print(u[18])
    # print(v[18])
    # print(u[19])
    # print(v[19])
    # print(u[20])
    # print(v[20])
    # print(u[21])
    # print(v[21])
    # print(u[22])
    # print(v[22])
    # print(u[23])
    # print(v[23])
    # print(u[24])
    # print(v[24])
    # print(u[25])
    # print(v[25])
    # print(u[26])
    # print(v[26])
    # print(u[27])
    # print(v[27])
    # print(u[28

=======
Suggestion 6

def dfs(u, p):
    for v in edge[u]:
        if v == p:
            continue
        path.append(v)
        dfs(v, u)
        path.append(u)

n, x, y = map(int, input().split())
edge = [[] for i in range(n+1)]
for i in range(n-1):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)
path = [x]
dfs(x, 0)
path.append(x)
path = path[path.index(y):]
print(*path)

=======
Suggestion 7

def main():
    n,x,y = map(int,input().split())
    n -= 1
    x -= 1
    y -= 1
    edges = [list(map(int,input().split())) for _ in range(n)]
    edges.sort(key=lambda x:x[0])
    edges.sort(key=lambda x:x[1])
    print(edges)
    print(x,y)
    for i in range(n):
        if edges[i][0] == x:
            print(edges[i][0],edges[i][1])
            x = edges[i][1]
        elif edges[i][1] == x:
            print(edges[i][0],edges[i][1])
            x = edges[i][0]
        if edges[i][0] == y:
            print(edges[i][0],edges[i][1])
            y = edges[i][1]
        elif edges[i][1] == y:
            print(edges[i][0],edges[i][1])
            y = edges[i][0]

=======
Suggestion 8

def main():
    n,x,y = map(int,input().split())
    tree = []
    for i in range(n-1):
        u,v = map(int,input().split())
        tree.append((u,v))
    #print(tree)
    path = []
    path.append(x)
    while True:
        for i in range(len(tree)):
            if tree[i][0] == x:
                x = tree[i][1]
                path.append(x)
                break
            if tree[i][1] == x:
                x = tree[i][0]
                path.append(x)
                break
        if x == y:
            break
    print(*path)

=======
Suggestion 9

def get_tree_paths(tree, start, end):
    paths = []
    for i in range(len(tree)):
        if tree[i][0] == start:
            if tree[i][1] == end:
                paths.append([start, end])
            else:
                sub_paths = get_tree_paths(tree, tree[i][1], end)
                for sub_path in sub_paths:
                    paths.append([start] + sub_path)
        elif tree[i][1] == start:
            if tree[i][0] == end:
                paths.append([start, end])
            else:
                sub_paths = get_tree_paths(tree, tree[i][0], end)
                for sub_path in sub_paths:
                    paths.append([start] + sub_path)
    return paths
