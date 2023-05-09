def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(1, N):
        A[i] += A[i-1]
    for i in range(1, M):
        B[i] += B[i-1]
    ans, j = 0, M
    for i in range(N):
        if A[i] > K:
            break
        while j > 0 and A[i] + B[j-1] > K:
            j -= 1
        ans = max(ans, i + j + 1)
    print(ans)
