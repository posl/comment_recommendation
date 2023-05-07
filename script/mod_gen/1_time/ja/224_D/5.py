def main():
    #入力
    M = int(input())
    G = [[0] * 9 for i in range(9)]
    for i in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u][v] = 1
        G[v][u] = 1
    P = list(map(int, input().split()))
    P = [i - 1 for i in P]
    #print(G)
    #print(P)
    
    #頂点 0 からの最短距離を求める
    dist = [0] * 9
    dist[0] = 1
    queue = [0]
    while queue:
        v = queue.pop(0)
        for i in range(9):
            if G[v][i] and dist[i] == 0:
                dist[i] = dist[v] + 1
                queue.append(i)
    #print(dist)
    
    #頂点 0 からの最短距離が偶数の頂点について、
    #コマが置かれていない頂点にコマを移動させる
    for i in range(9):
        if dist[i] % 2 == 0:
            P[i] = -1
    #print(P)
    
    #コマが置かれていない頂点にコマが置かれている頂点から移動させる
    ans = 0
    for i in range(9):
        if P[i] == -1:
            for j in range(9):
                if P[j] == i:
                    P[j] = -1
                    ans += 1
    #print(P)
    
    #コマが置かれている頂点の番号が頂点の番号と一致しているか判定
    for i in range(9):
        if P[i] != -1 and P[i] != i:
            ans = -1
            break
    print(ans)
main()

if __name__ == '__main__':
    main()