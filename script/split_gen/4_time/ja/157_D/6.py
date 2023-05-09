def main():
    # 入力
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    
    # 友達候補数
    ans = [0] * N
    
    # 友達関係を表すグラフ
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    
    # ブロック関係を表すグラフ
    B = [[] for _ in range(N)]
    for c, d in CD:
        B[c - 1].append(d - 1)
        B[d - 1].append(c - 1)
    
    # 各人の友達候補数を求める
    for i in range(N):
        # 自分自身は除外
        ans[i] = len(set(G[i]) - set(B[i])) - 1
    
    # 出力
    print(*ans)
