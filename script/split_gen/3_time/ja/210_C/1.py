def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    # 累積和
    C_sum = [0]*(N+1)
    for i in range(N):
        C_sum[i+1] = C_sum[i] + C[i]
    # 連続するK個のキャンディの色の種類数を求める
    candy_set = set()
    for i in range(N-K+1):
        candy_set.add(C_sum[i+K] - C_sum[i])
    print(len(candy_set))
