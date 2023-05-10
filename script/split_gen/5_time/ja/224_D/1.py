def main():
    # データ入力
    M = int(input())
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    p = list(map(int, input().split()))
    # 頂点とコマの対応関係を記録する配列
    p_to_v = [0] * 9
    for i in range(8):
        p_to_v[p[i]] = i + 1
    # 隣接リストを作成する
    adj = [[] for _ in range(9)]
    for i in range(M):
        adj[u[i]].append(v[i])
        adj[v[i]].append(u[i])
    # 頂点 1 から順に、その頂点にあるコマを目的の位置に移動させる
    ans = 0
    for i in range(1, 9):
        # 頂点 i にあるコマの目的の位置を j とする
        j = p_to_v[i]
        # 頂点 i に隣接する頂点にあるコマを頂点 i に移動させる
        for v in adj[i]:
            if p_to_v[v] == i:
                continue
            k = p_to_v[v]
            p_to_v[v] = i
            p_to_v[i] = k
            ans += 1
            # 頂点 j にあるコマを頂点 v に移動させる
            p_to_v[k] = j
            p_to_v[j] = k
            ans += 1
            break
    # 答えを出力する
    print(ans)
