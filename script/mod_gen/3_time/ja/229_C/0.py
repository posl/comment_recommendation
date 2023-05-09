def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #A[i]の値が小さい順に並べ替える
    A, B = zip(*sorted(zip(A, B)))
    #Bの累積和を求める
    B_sum = [0] * (N + 1)
    for i in range(N):
        B_sum[i + 1] = B_sum[i] + B[i]
    #A[i]の値について、Bの累積和の最大値を求める
    B_sum_max = [0] * (N + 1)
    B_sum_max[N] = B_sum[N]
    for i in range(N - 1, -1, -1):
        B_sum_max[i] = max(B_sum_max[i + 1], B_sum[i + 1])
    #A[i]の値について、A[i] * B[j]の最大値を求める
    A_B_max = [0] * (N + 1)
    for i in range(N):
        A_B_max[i + 1] = max(A_B_max[i], A[i] * B[i])
    #A[i]の値について、A[i] * B[j] + B_sum[j]の最大値を求める
    A_B_B_sum_max = [0] * (N + 1)
    for i in range(N):
        A_B_B_sum_max[i + 1] = max(A_B_B_sum_max[i], A_B_max[i + 1] + B_sum_max[i + 1])
    #A[i]の値について、A[i] * B[j] + B_sum[j]がWを超えない最大値を求める
    A_B_B_sum_W_max = [0] * (N + 1)
    for i in range(N):
        if A[i] * B_sum[N] <= W:
            A_B_B_sum_W_max[i + 1] =

if __name__ == '__main__':
    main()