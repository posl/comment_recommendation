def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    for i in range(N-1):
        ans += A[i] * sum(A[i+1:])
        ans %= MOD
    print(ans)
