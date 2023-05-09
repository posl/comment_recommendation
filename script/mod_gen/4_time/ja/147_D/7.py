def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        bit = 0
        for j in range(n):
            if a[j] >> i & 1:
                bit += 1
        ans += bit * (n - bit) * pow(2, i, mod)
        ans %= mod
    print(ans)
solve()

if __name__ == '__main__':
    solve()