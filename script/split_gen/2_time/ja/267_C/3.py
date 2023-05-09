def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(M):
        B[i] = A[i]
    for i in range(M, N):
        B[i] = B[i - 1] + A[i]
    ans = 0
    for i in range(M, N):
        ans = max(ans, B[i] - B[i - M])
    print(ans)
