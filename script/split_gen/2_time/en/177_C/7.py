def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    ans = 0
    Asum = sum(A)
    for i in range(N):
        Asum -= A[i]
        ans += A[i] * Asum
        ans %= MOD
    print(ans)
