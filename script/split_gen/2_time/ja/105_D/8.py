def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和のリスト
    sum_list = [0]
    for i in range(N):
        sum_list.append(sum_list[i] + A[i])
    
    # 各余りの数
    remainders = [0] * M
    for i in range(N+1):
        remainders[sum_list[i] % M] += 1
    # 組み合わせ
    ans = 0
    for i in range(M):
        ans += remainders[i] * (remainders[i] - 1) // 2
    print(ans)
