def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sum = [0] * (N + 1)
    A_sum[0] = 0
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    #print(A_sum)
    min_diff = 10 ** 9
    for i in range(2, N - 1):
        for j in range(1, i):
            P = A_sum[j]
            Q = A_sum[i] - A_sum[j]
            for k in range(i + 1, N):
                R = A_sum[k] - A_sum[i]
                S = A_sum[N] - A_sum[k]
                max_num = max(P, Q, R, S)
                min_num = min(P, Q, R, S)
                min_diff = min(min_diff, max_num - min_num)
    print(min_diff)

if __name__ == '__main__':
    main()