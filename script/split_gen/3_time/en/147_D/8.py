def solve(n, A):
    MOD = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for a in A:
            if a & (1<<i):
                cnt += 1
        ans += (1<<i) * cnt * (n-cnt)
        ans %= MOD
    return ans
n = int(input())
A = list(map(int, input().split()))
print(solve(n, A))
