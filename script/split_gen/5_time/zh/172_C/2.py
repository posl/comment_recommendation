def solve():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = [0] + A
    B = [0] + B
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    for i in range(1, M + 1):
        B[i] += B[i - 1]
    ans = 0
    j = M
    for i in range(N + 1):
        if A[i] > K:
            break
        while A[i] + B[j] > K:
            j -= 1
        ans = max(ans, i + j)
    print(ans)
