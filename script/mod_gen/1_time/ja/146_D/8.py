def main():
    N = int(input())
    #各頂点の隣接リスト
    edge = [[] for _ in range(N+1)]
    #各頂点の隣接リストを作成
    for _ in range(N-1):
        a,b = map(int,input().split())
        edge[a].append(b)
        edge[b].append(a)
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の塗り分けの色
    color = [0]*(N+1)
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の隣接リストを頂点番号の小さい

if __name__ == '__main__':
    main()