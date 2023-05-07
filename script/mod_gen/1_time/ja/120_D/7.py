def main():
    # 標準入力から値を取得する
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # 隣接リスト
    G = [[] for _ in range(N+1)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)
    # グラフGにおいて、頂点1からの最短距離を求める
    # 計算量はO(N+M)
    from collections import deque
    dist = [-1] * (N+1)
    dist[1] = 0
    que = deque([1])
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                que.append(nv)
    # 崩落する橋の順番を逆順にして、順番に橋を崩落させる
    # 計算量はO(M)
    ans = []
    for a, b in reversed(AB):
        # 橋(a, b)を崩落させる
        # ただし、aからbへの橋を崩落させたとき、
        # aからの最短距離がbからの最短距離よりも大きい場合は、
        # aからの最短距離をbからの最短距離と同じにする
        if dist[a] == dist[b] + 1:
            ans.append(dist[a] * (N - dist[a]))
        else:
            ans.append(dist[a] * (N - dist[a]))
            dist[a] = dist[b] + 1
    # 崩落する橋の順番を逆順にして出力する
    # 計算量はO(M)
    for a in reversed(ans):
        print(a)

if __name__ == '__main__':
    main()