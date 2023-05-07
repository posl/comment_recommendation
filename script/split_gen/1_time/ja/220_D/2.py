def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    ans[A[0]] = 1
    for i in range(1,N):
        B = [0] * 10
        for j in range(10):
            B[(j+A[i])%10] += ans[j]
            B[(j*A[i])%10] += ans[j]
        for j in range(10):
            B[j] %= MOD
        ans = B
    for i in range(10):
        print(ans[i])
