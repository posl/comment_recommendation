def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * A[i] * (N - i - 1)
        ans %= 10**9 + 7
    for i in range(N - 1, 0, -1):
        ans += A[i] * A[i] * i
        ans %= 10**9 + 7
    for i in range(N - 1):
        ans -= A[i] * A[i + 1] * 2
        ans %= 10**9 + 7
    print(ans)
