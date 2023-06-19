def solve(a, n):
    s = str(n)
    ans = 0
    while True:
        if s == '1':
            return ans
        if s[-1] == '0':
            s = s[:-1]
        else:
            s = str(int(s) * a)
        ans += 1
        if len(s) > 6:
            return -1
