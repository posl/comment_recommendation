def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # 重さが大きい順にソート
    A, B = zip(*sorted(zip(A, B), reverse=True))
    # 累積和をとる
    B = list(accumulate(B))
    # おいしさの最大値を求める
    ans = 0
    for i in range(N):
        # 重さが W を超えたら終了
        if A[i] * B[i] > W:
            break
        # 重さが W 以下のときは、おいしさの最大値を更新
        ans = max(ans, A[i] * B[i])
    # 重さが W を超えたときは、おいしさの最大値を更新
    ans = max(ans, (W - B[i]) * A[i] // B[i])
    print(ans)
