def main():
    #入力
    N,Q = map(int,input().split())
    #隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        a,b = a-1,b-1
        adj[a].append(b)
        adj[b].append(a)
    #各頂点のカウンターの値
    counter = [0]*N
    for _ in range(Q):
        p,x = map(int,input().split())
        p = p-1
        counter[p] += x
    #深さ優先探索
    stack = [0]
    visited = [False]*N
    while stack:
        v = stack.pop()
        visited[v] = True
        for w in adj[v]:
            if visited[w]:
                continue
            counter[w] += counter[v]
            stack.append(w)
    #出力
    print(" ".join(map(str,counter)))
