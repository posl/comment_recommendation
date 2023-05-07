def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    MOD = 10**9+7
    ans = 0
    for i in range(N-1):
        ans += A[i] * (A[i+1] - A[i]) * (N - i - 1)
        ans %= MOD
    print(ans)
