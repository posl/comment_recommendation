def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] % M == 0:
            A[i] = int(A[i] / M)
        else:
            A[i] = A[i] % M
    for i in range(1, N):
        A[i] = A[i] + A[i - 1]
    A = [0] + A
    B = [0] * M
    for i in range(N + 1):
        B[A[i] % M] += 1
    ans = 0
    for i in range(M):
        ans += B[i] * (B[i] - 1) // 2
    print(ans)
