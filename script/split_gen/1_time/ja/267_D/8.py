def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 1. Aの累積和を求める
    # 2. 1.の累積和の差を求める
    # 3. 2.の差の累積和の最大値を求める
    # 4. 3.の最大値を出力
    # 1.
    A_sum = [0] * (N + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    # 2.
    A_diff = [0] * N
    for i in range(N - 1):
        A_diff[i + 1] = A_sum[i + 1] - A_sum[i]
    # 3.
    A_diff_sum = [0] * (N + 1)
    for i in range(N):
        A_diff_sum[i + 1] = A_diff_sum[i] + A_diff[i]
    # 4.
    max_sum = 0
    for i in range(M, N + 1):
        max_sum = max(max_sum, A_diff_sum[i] - A_diff_sum[i - M])
    print(max_sum)
