def solve(s,t):
    res = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            res += 1
    return res

if __name__ == '__main__':
    solve()