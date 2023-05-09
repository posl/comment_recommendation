def main():
    M = int(input())
    edge = []
    for i in range(M):
        edge.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    #print(edge)
    #print(p)
    # グラフの作成
    G = [[] for i in range(9)]
    for e in edge:
        G[e[0]-1].append(e[1]-1)
        G[e[1]-1].append(e[0]-1)
    #print(G)
    # グラフの頂点ごとにコマの数を数える
    cnt = [0 for i in range(9)]
    for i in range(8):
        cnt[p[i]-1] += 1
    #print(cnt)
    # 頂点のコマの数が 1 以上 2 以下であることを確認する
    for i in range(9):
        if cnt[i] >= 3:
            print(-1)
            return
    # 頂点のコマの数が 2 の場合、その頂点と隣接する頂点にコマが存在することを確認する
    for i in range(9):
        if cnt[i] == 2:
            for j in G[i]:
                if cnt[j] == 0:
                    print(-1)
                    return
    # 頂点のコマの数が 1 の場合、その頂点と隣接する頂点にコマが存在することを確認する
    for i in range(9):
        if cnt[i] == 1:
            for j in G[i]:
                if cnt[j] == 0:
                    print(-1)
                    return
    # 頂点のコマの数が 0 の場合、その頂点と隣接する頂点にコマが存在することを確認する
    for i in range(9):
        if cnt[i] == 0:
            for j in G[i]:
                if cnt[j] == 0:
                    print(-1)
                    return
    # 頂点のコマの数が 1

if __name__ == '__main__':
    main()