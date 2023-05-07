def main():
    N, M, K = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    for i in range(1, M + 1):
        B[i] += B[i - 1]
    ans = 0
    j = M
    for i in range(N + 1):
        if A[i] > K:
            break
        while B[j] > K - A[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

if __name__ == '__main__':
    main()