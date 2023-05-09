def main():
    #入力
    N,Q = map(int,input().split())
    a = [0] * (N-1)
    b = [0] * (N-1)
    for i in range(N-1):
        a[i],b[i] = map(int,input().split())
    p = [0] * Q
    x = [0] * Q
    for i in range(Q):
        p[i],x[i] = map(int,input().split())
    #処理
    #頂点のカウンターの値
    c = [0] * N
    #隣接リスト
    G = [[] for i in range(N)]
    for i in range(N-1):
        G[a[i]-1].append(b[i]-1)
        G[b[i]-1].append(a[i]-1)
    #隣接リストを根から探索
    #根から隣接する頂点に x を足す
    #隣接する頂点からさらに隣接する頂点に x を足す
    #...
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #...
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #...
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #...
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #...
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #隣接する頂点に x を足

if __name__ == '__main__':
    main()