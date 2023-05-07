def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j]>>i & 1:
                cnt += 1
        ans = (ans + (1<<i) * cnt * (n-cnt)) % mod
    print(ans)
