def main():
    N = int(input())
    W = list(map(int, input().split()))
    # 累積和を求める
    W_sum = [0] * (N+1)
    for i in range(N):
        W_sum[i+1] = W_sum[i] + W[i]
    # 差の絶対値の最小値を求める
    ans = float("inf")
    for T in range(1, N):
        ans = min(ans, abs(W_sum[T] - (W_sum[N] - W_sum[T])))
    print(ans)

if __name__ == '__main__':
    main()