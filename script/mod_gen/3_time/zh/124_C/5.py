def solve(s):
    if len(s) == 1:
        return 0
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    if s[0] == s[1]:
        return 1 + solve(s[1:])
    else:
        return solve(s[1:])

if __name__ == '__main__':
    solve()