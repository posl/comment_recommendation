def main():
    # Read input
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # Calculate cumulative sum of A and B
    A_sum = [0] * (N + 1)
    B_sum = [0] * (M + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    for i in range(M):
        B_sum[i + 1] = B_sum[i] + B[i]
    # Calculate the maximum number of books that can be read
    max_num = 0
    j = M
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        while B_sum[j] > K - A_sum[i]:
            j -= 1
        max_num = max(max_num, i + j)
    # Output the answer
    print(max_num)

if __name__ == '__main__':
    main()