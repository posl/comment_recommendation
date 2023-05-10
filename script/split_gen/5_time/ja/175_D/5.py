def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # 1回移動した時の最大値を求める
    max_score = -10**18
    for i in range(N):
        score = 0
        next = i
        for j in range(K):
            next = P[next] - 1
            score += C[next]
            max_score = max(max_score, score)
    # 1回移動した時の最大値が正の場合、
    # K回移動した時の最大値は、
    # K回移動した時の最大値 = (K // N) * (1回移動した時の最大値) + (K % N)回移動した時の最大値
    if max_score > 0:
        # K回移動した時の最大値 = (K // N) * (1回移動した時の最大値) + (K % N)回移動した時の最大値
        # (K // N) * (1回移動した時の最大値) は、K回移動した時の最大値の候補の一つ
        # (K % N)回移動した時の最大値は、
        # 1回移動した時の最大値から、(K % N)回移動した時の最大値を求める
        # (K % N)回移動した時の最大値は、
        # 1回移動した時の最大値から、(K % N)回移動した時の最大値を求める
        # 1回移動した時の最大値は、
        # 1回移動した時の最大値から、(K % N)回移動した時の最大値を求める
        # 1回移動した時の最大値は、
        # 1回移動した時の最大値
