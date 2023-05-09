def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = (i + 1) * A[i] - (i) * A[i]
    ans = 0
    for i in range(N - M + 1):
        ans = max(ans, sum(B[i:i + M]))
    print(ans)
