def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * A[i] * (N - 1)
        ans %= 1000000007
    for i in range(N):
        for j in range(i + 1, N):
            ans -= 2 * A[i] * A[j]
            ans %= 1000000007
    print(ans)
