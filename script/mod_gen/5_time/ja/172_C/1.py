def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_sum = [0] * (N + 1)
    B_sum = [0] * (M + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    for i in range(M):
        B_sum[i + 1] = B_sum[i] + B[i]
    ans = 0
    j = M
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        while A_sum[i] + B_sum[j] > K:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

if __name__ == '__main__':
    main()