def solve(s):
    n = len(s)
    r = 0
    b = 0
    for i in range(n):
        if s[i] == '0':
            r += 1
        else:
            b += 1
    return min(r, b) * 2
print(solve(input()))
