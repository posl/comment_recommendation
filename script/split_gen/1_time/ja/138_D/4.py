def main():
    #入力
    n,q = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n-1)]
    px = [list(map(int,input().split())) for _ in range(q)]
    #隣接リストを作成
    graph = [[] for _ in range(n+1)]
    for a,b in ab:
        graph[a].append(b)
        graph[b].append(a)
    #累積和
    val = [0]*(n+1)
    for p,x in px:
        val[p] += x
    #DFS
    queue = [1]
    seen = [False]*(n+1)
    seen[1] = True
    while queue:
        v = queue.pop()
        for i in graph[v]:
            if seen[i]:
                continue
            val[i] += val[v]
            seen[i] = True
            queue.append(i)
    #出力
    print(*val[1:])
