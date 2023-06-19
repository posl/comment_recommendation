def solve(n, a):
    ans = 0
    for i in range(60):
        c = 0
        for j in range(n):
            if a[j] & 1:
                c += 1
            a[j] >>= 1
        ans += c * (n - c) * (1 << i)
        ans %= 10 ** 9 + 7
    return ans

if __name__ == '__main__':
    solve()