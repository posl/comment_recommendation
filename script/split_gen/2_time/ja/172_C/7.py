def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 机Aの本を読むのにかかる時間の累積和
    A_sum = [0]
    for a in A:
        A_sum.append(A_sum[-1] + a)
    # 机Bの本を読むのにかかる時間の累積和
    B_sum = [0]
    for b in B:
        B_sum.append(B_sum[-1] + b)
    # 机Aの本を読むのにかかる時間の累積和がKを超える最小のindex
    A_index = 0
    # 机Bの本を読むのにかかる時間の累積和がKを超える最小のindex
    B_index = 0
    # 机Aの本を読むのにかかる時間の累積和がKを超える最小のindexを求める
    while A_index < N + 1:
        if A_sum[A_index] > K:
            break
        A_index += 1
    # 机Bの本を読むのにかかる時間の累積和がKを超える最小のindexを求める
    while B_index < M + 1:
        if B_sum[B_index] > K:
            break
        B_index += 1
    # 机Aの本を読むのにかかる時間の累積和がKを超える最小のindexを1減らす
    A_index -= 1
    # 机Bの本を読むのにかかる時間の累積和がKを超える最小のindexを1減らす
    B_index -= 1
    # 机Aの本を読むのにかかる時間の累積和がKを超える最小のindexと机Bの本を読むのにかかる時間の累
