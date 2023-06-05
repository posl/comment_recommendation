def solve(n, x, s):
    ans = x
    for c in s:
        if c == 'U':
            ans = ans // 2
        elif c == 'L':
            ans = ans * 2 - 1
        else:
            ans = ans * 2 + 1
    return ans
