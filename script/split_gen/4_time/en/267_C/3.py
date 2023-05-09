def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] + B[i-1]
    ans = 0
    for i in range(M-1, N):
        ans = max(ans, B[i] - B[i-M])
    print(ans)
