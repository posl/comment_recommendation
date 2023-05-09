def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    sumA = sum(A)%mod
    for i in range(N-1):
        sumA -= A[i]
        ans += A[i]*sumA
        ans %= mod
    print(ans)
