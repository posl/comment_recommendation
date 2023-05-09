def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    # 累積和を作る
    sum_list = [0]
    for i in range(1, N + 2):
        sum_list.append(sum_list[i - 1] + i)
    # 答えを求める
    ans = 0
    for i in range(K, N + 2):
        ans += sum_list[i] - sum_list[i - K] + 1
        ans %= MOD
    print(ans)
