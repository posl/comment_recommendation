def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # Aの累積和を求める
    A_sum = [0] * (N + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    # Bの累積和を求める
    B_sum = [0] * (M + 1)
    for i in range(M):
        B_sum[i + 1] = B_sum[i] + B[i]
    # Bの累積和をK以下になるようにする
    B_sum = [x for x in B_sum if x <= K]
    # Aの累積和をK以下になるようにする
    # そのときのBの累積和の最大値を求める
    ans = 0
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        j = bisect.bisect_right(B_sum, K - A_sum[i])
        ans = max(ans, i + j)
    print(ans)

if __name__ == '__main__':
    main()