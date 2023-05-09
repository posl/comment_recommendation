def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    # 3日目までの合計点
    S = [p[0] + p[1] + p[2] for p in P]
    # 4日目の得点
    T = [300 - p[3] for p in P]
    # 4日目の得点でソート
    T_sorted = sorted(T)
    # 4日目の得点でソートしたときの順位
    rank = [0] * N
    for i, t in enumerate(T_sorted):
        rank[T.index(t)] = i + 1
    # 3日目までの合計点でソート
    S_sorted = sorted(S)
    # 4日目の得点でソートしたときの順位と、3日目までの合計点でソートしたときの順位の差がK以下であればYes
    for i in range(N):
        if rank[i] - S_sorted.index(S[i]) <= K:
            print("Yes")
        else:
            print("No")
