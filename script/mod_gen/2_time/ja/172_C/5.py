def main():
    #入力
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #累積和
    A_sum = [0] * (N + 1)
    B_sum = [0] * (M + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    for i in range(M):
        B_sum[i + 1] = B_sum[i] + B[i]
    #本の数を数える
    ans = 0
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        j = M
        while B_sum[j] > K - A_sum[i]:
            j -= 1
        ans = max(ans, i + j)
    #出力
    print(ans)

if __name__ == '__main__':
    main()