def solve(s):
    s = list(s)
    ans = 0
    while True:
        if len(s) == 0:
            break
        if s[0] == s[-1]:
            ans += 1
            s = s[1:-1]
        else:
            break
    return ans

if __name__ == '__main__':
    solve()