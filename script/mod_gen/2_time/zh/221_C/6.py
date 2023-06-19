def solve(n):
    s = str(n)
    l = len(s)
    ans = 0
    for i in range(1, l):
        a = int(s[:i])
        b = int(s[i:])
        ans = max(ans, a * b)
    return ans

if __name__ == '__main__':
    solve()