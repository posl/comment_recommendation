def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    # Aの間隔を全て求める
    D = []
    for i in range(N-1):
        D.append(A[i+1]-A[i]-1)
    # Aの間隔の累積和を求める
    D_sum = [0]
    for i in range(N-1):
        D_sum.append(D_sum[i] + D[i])
    # 答えを求める
    for k in K:
        # Aの間隔の累積和がk-1以下の最大のindexを求める
        # indexがiならA[i]とA[i+1]の間にk番目の数がある
        # indexがiならA[i]とA[i+1]の間にk番目の数がある
        i = len(D) - 1 - D_sum[::-1].index(max([0, k-1]))
        # A[i]とA[i+1]の間にk番目の数がある
        # A[i]とA[i+1]の間にk番目の数がある
        print(A[i] + k - D_sum[i])

if __name__ == '__main__':
    main()