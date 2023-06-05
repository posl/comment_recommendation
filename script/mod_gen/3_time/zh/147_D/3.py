def solve():
    n = int(input())
    a = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    for i in range(60):
        mask = 1 << i
        count = 0
        for j in range(n):
            if a[j] & mask:
                count += 1
        ans += (count * (n-count) * mask) % MOD
    print(ans % MOD)

if __name__ == '__main__':
    solve()