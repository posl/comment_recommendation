def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 進んだ距離の累積和を求める
    A_sum = [0] * (N + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    # 累積和の最大値を求める
    A_sum_max = [0] * (N + 1)
    for i in range(N + 1):
        A_sum_max[i] = max(A_sum_max[i - 1], A_sum[i])
    # 累積和の最小値を求める
    A_sum_min = [0] * (N + 1)
    for i in range(N + 1):
        A_sum_min[i] = min(A_sum_min[i - 1], A_sum[i])
    # 最大値と最小値の差の最大値を求める
    ans = 0
    for i in range(N + 1):
        ans = max(ans, A_sum_max[i] - A_sum_min[i])
    print(ans)

if __name__ == '__main__':
    main()