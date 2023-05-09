def main():
    #入力
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    #辺の有無を判定するためのリスト
    edge = [[0] * N for _ in range(N)]
    for i in range(M):
        edge[AB[i][0] - 1][AB[i][1] - 1] = 1
        edge[AB[i][1] - 1][AB[i][0] - 1] = 1
    #print(edge)
    #頂点1から頂点Nまでの各頂点が赤、緑、青のいずれかで塗られている場合の数
    ans = 1
    for i in range(N):
        #頂点iから頂点i+1までの各頂点が赤、緑、青のいずれかで塗られている場合の数
        ans *= 3
    #print(ans)
    #頂点iから頂点i+1までの各頂点が赤、緑、青のいずれかで塗られている場合の数から、条件を満たさない場合の数を引く
    for i in range(N):
        for j in range(i + 1, N):
            if edge[i][j] == 1:
                #頂点iと頂点jが辺で直接結ばれている場合
                ans -= 3
    #print(ans)
    #頂点iと頂点jが辺で直接結ばれている場合の数を引く
    for i in range(M):
        for j in range(i + 1, M):
            if edge[AB[i][0] - 1][AB[j][0] - 1] == 1 and edge[AB[i][0] - 1][AB[j][1] - 1] == 1 and edge[AB[i][1] - 1][

if __name__ == '__main__':
    main()