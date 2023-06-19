Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def dfs(G, v, c):
    color[v] = c
    for t in G[v]:
        if color[t] == c:
            return False
        if color[t] == 0 and not dfs(G, t, -c):
            return False
    return True

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

color = [0] * N

=======
Suggestion 3

def dfs(v):
    global color
    global flag
    color[v] = 1
    for i in range(len(edge[v])):
        if color[edge[v][i]] == 0:
            dfs(edge[v][i])
        elif color[edge[v][i]] == 2:
            flag = False
    color[v] = 2

n,m = map(int,input().split())
edge = [[] for i in range(n)]
for i in range(m):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
color = [0]*n
ans = 0
for i in range(n):
    if color[i] == 0:
        flag = True
        dfs(i)
        if flag:
            ans += 1
print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
    edges.sort()
    # print(edges)
    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            u1, v1 = edges[i]
            u2, v2 = edges[j]
            if u1 == u2 or u1 == v2 or v1 == u2 or v1 == v2:
                continue
            ans += 1
    print(ans)

=======
Suggestion 5

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    d = {}
    for i in range(m):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        if a not in d:
            d[a] = []
        d[a].append(b)
    ans = 0
    for i in range(1, n+1):
        if i not in d:
            continue
        for j in range(i+1, n+1):
            if j not in d:
                ans += 1
            elif j not in d[i]:
                ans += 1
    print(ans)

=======
Suggestion 7

def solve():
    n,m=map(int,input().split())
    edge=[]
    for _ in range(m):
        u,v=map(int,input().split())
        edge.append((u,v))
    edge.sort()
    ans=0
    cnt=1
    for i in range(1,m):
        if edge[i]==edge[i-1]:
            cnt+=1
        else:
            ans+=cnt*(cnt-1)//2
            cnt=1
    ans+=cnt*(cnt-1)//2
    print(n*(n-1)//2-ans)

=======
Suggestion 8

def solve():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    print(n, m)
    print(edges)
    # 1. 逆向思维，先计算出所有的组合，然后排除掉不符合条件的组合
    # 2. 逆向思维，先找出所有不符合条件的组合，然后用总的组合数减去不符合条件的组合数
    # 3. 逆向思维，先找出所有符合条件的组合，然后用总的组合数减去符合条件的组合数
    # 4. 逆向思维，先找出所有符合条件的组合，然后用总的组合数减去符合条件的组合数
    # 5. 逆向思维，先找出所有符合条件的组合，然后用总的组合数减去符合条件的组合数

    # 1. 逆向思维，先计算出所有的组合，然后排除掉不符合条件的组合
    # 2. 逆向思维，先找出所有不符合条件的组合，然后用总的组合数减去不符合条件的组合数
    # 3. 逆向思维，先找出所有符合条件的组合，然后用总的组合数减去符合条件的组合数
    # 4. 逆向思维，先找出所有符合条件的组合，然后用总的组合数减去符合条件的组合数
    # 5. 逆向思维，先找出所有符合条件的组合，然后用总的组合数减去符合条件的组合数

    # 1. 逆向思维，先计算出所有的组合，然后排除掉不符合条件的组合
    #

=======
Suggestion 9

def main():
    # 读取输入
    N, M = map(int, input().split())
    # 读取M条边
    edges = []
    for i in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
    # 计算答案
    ans = 0
    for u, v in edges:
        # 判断是否可以形成双线图
        # 双线图的定义是：没有一条边连接到涂成相同颜色的顶点。
        # 也就是说，如果u和v的颜色相同，那么u和v之间不能有边。
        # 也就是说，如果u和v之间有边，那么u和v的颜色必须不同。
        # 所以，如果u和v的颜色相同，那么u和v之间不能有边。
        # 所以，如果u和v之间有边，那么u和v的颜色必须不同。
        # 所以，如果u和v的颜色相同，那么u和v之间不能有边。
        # 所以，如果u和v之间有边，那么u和v的颜色必须不同。
        # 所以，如果u和v的颜色相同，那么u和v之间不能有边。
        # 所以，如果u和v之间有边，那么u和v的颜色必须不同。
        # 所以，如果u和v的颜色相同，那么u和v之间不能有边。
        # 所以，如果u和v之间有边，那么u和v的颜色必须不同。
        # 所以，如果u和v的颜色相同，那么u和v之间不能有边。
        # 所以，如果u和v之间有边，那么u和v的颜色必
