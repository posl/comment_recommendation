def main():
    import sys
    input = sys.stdin.readline
    #入力
    N, M = map(int, input().split())
    #u, vを格納する配列
    u = [0] * M
    v = [0] * M
    #u, vを格納
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    
    #頂点がN個あるので、N個の配列を用意する
    #1, 2, ..., N の番号が付いている
    #各頂点の次数を格納する配列
    deg = [0] * N
    for i in range(M):
        #辺の始点と終点を格納
        #辺の始点はu[i] - 1
        #辺の終点はv[i] - 1
        #u[i]とv[i]の次数をそれぞれ1増やす
        deg[u[i] - 1] += 1
        deg[v[i] - 1] += 1
    
    #パスグラフなら、次数が2でない頂点が存在しない
    #次数が2でない頂点が存在するならNo
    #存在しないならYes
    for i in range(N):
        if deg[i] != 2:
            print("No")
            return
    
    #全ての頂点の次数が2ならYes
    print("Yes")
