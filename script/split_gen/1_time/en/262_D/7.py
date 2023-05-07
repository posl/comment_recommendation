def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for bit in range(1, 1 << N):
        prod = 1
        cnt = 0
        for i in range(N):
            if bit & (1 << i):
                prod *= A[i]
                cnt += 1
        if prod % cnt == 0:
            ans += 1
    print(ans % MOD)
