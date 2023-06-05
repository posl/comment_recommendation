def solve(s):
    if len(s) == 1:
        return 0
    else:
        if s[0] == '0' and s[1] == '0':
            return 1 + solve(s[1:])
        elif s[0] == '1' and s[1] == '1':
            return 1 + solve(s[1:])
        else:
            return solve(s[1:])
