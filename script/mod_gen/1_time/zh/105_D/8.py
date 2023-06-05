def solve(n, m, a):
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    t = [x % m for x in s]
    from collections import defaultdict
    d = defaultdict(int)
    for x in t:
        d[x] += 1
    ans = 0
    for k, v in d.items():
        ans += v * (v - 1) // 2
    return ans

if __name__ == '__main__':
    solve()