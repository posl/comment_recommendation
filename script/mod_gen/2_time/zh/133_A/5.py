def C(n, r):
    if n == 0 or r == 0:
        return 1
    if r > n:
        return 0
    if n == r:
        return 1
    if n - r < r:
        r = n - r
    return C(n - 1, r - 1) * n // r
n, k = map(int, input().split())
MOD = 10**9 + 7
for i in range(1, k + 1):
    ans = C(n - k + 1, i) * C(k - 1, i - 1) % MOD
    print(ans)

if __name__ == '__main__':
    C()