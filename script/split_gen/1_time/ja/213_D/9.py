def main():
    N = int(input())
    A = []
    B = []
    for i in range(N-1):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A,B)
    #頂点1からの距離を求める
    dist = [0] * (N+1)
    #print(dist)
    #頂点1からの距離を求める
    def dfs(v, p, d):
        dist[v] = d
        for u in E[v]:
            if u == p:
                continue
            dfs(u, v, d + 1)
    #辺のリスト
    E = [[] for _ in range(N+1)]
    for i in range(N-1):
        E[A[i]].append(B[i])
        E[B[i]].append(A[i])
    #print(E)
    dfs(1, -1, 0)
    #print(dist)
    #頂点1からの距離が奇数の頂点を取得
    odd = []
    for i in range(1,N+1):
        if dist[i]%2 == 1:
            odd.append(i)
    #print(odd)
    if len(odd) <= N//2:
        print(*[1] + odd)
    else:
        print(*[1] + [i for i in range(2,N+1) if i not in odd])
