def count200(N, A):
    # 200で割った余りをカウント
    C = [0] * 200
    for a in A:
        C[a % 200] += 1
    # 余りごとに組み合わせを数える
    ans = 0
    for c in C:
        ans += c * (c - 1) // 2
    return ans
