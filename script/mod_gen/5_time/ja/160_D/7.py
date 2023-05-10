def bfs():
    # 未探索の頂点を格納するスタック
    stack = []
    # 未探索の頂点をスタックに追加
    stack.append(1)
    # 未探索の頂点がなくなるまで繰り返す
    while len(stack) > 0:
        # スタックから頂点を取り出す
        v = stack.pop()
        # 頂点 v に隣接する頂点を全て調べる
        for i in range(len(g[v])):
            # 隣接する頂点が未探索の場合はスタックに追加
            if d[g[v][i]] == -1:
                # 頂点 g[v][i] に隣接する頂点をスタックに追加
                stack.append(g[v][i])
                # 頂点 g[v][i] に隣接する頂点の距離を更新
                d[g[v][i]] = d[v] + 1
n,x,y = map(int,input().split())
g = [[] for _ in range(n+1)]
for i in range(1,n):
    g[i].append(i+1)
    g[i+1].append(i)
g[x].append(y)
g[y].append(x)
d = [-1]*(n+1)
d[1] = 0
bfs()
for i in range(1,n):
    ans = 0
    for j in range(i+1,n+1):
        ans += d[j].count(i)
    print(ans)

if __name__ == '__main__':
    bfs()