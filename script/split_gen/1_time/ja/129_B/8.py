def main():
    N = int(input())
    W = list(map(int, input().split()))
    # 累積和
    W_sum = []
    W_sum.append(W[0])
    for i in range(1, N):
        W_sum.append(W_sum[i-1] + W[i])
    ans = 10000
    for i in range(1, N):
        ans = min(ans, abs(W_sum[i-1] - (W_sum[N-1] - W_sum[i-1])))
    print(ans)
