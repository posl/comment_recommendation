def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    # 累積和をとる
    p_sum = [0] * (N + 1)
    for i in range(N):
        p_sum[i + 1] = p_sum[i] + p[i]
    # print(N, K)
    # print(p)
    # print(p_sum)
    # 期待値の最大値を求める
    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, (p_sum[i + K] - p_sum[i]) / 2 + p_sum[i])
    print(ans)

if __name__ == '__main__':
    main()