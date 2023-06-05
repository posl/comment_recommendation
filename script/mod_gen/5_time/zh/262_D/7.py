def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if sum(A[i:j]) % (j-i) == 0:
                ans += 1
    print(ans % mod)
solve()
