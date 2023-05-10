def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1, N+1):
        for j in range(N-i+1):
            ans += sum(A[j:j+i])%i == 0
    print(ans%MOD)
