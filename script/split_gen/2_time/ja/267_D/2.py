def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(1, N + 1):
        B[i] = B[i - 1] + A[i - 1]
    ans = -2 * 10 ** 5 * 2000
    for i in range(N - M + 1):
        ans = max(ans, B[i + M] - B[i])
    print(ans)
