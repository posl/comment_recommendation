def solve(N, M, s, c):
    if N == 1:
        return c[0]
    elif N == 2:
        if s[0] == 1 and c[0] == 0:
            return -1
        else:
            return c[0] * 10 + c[1]
    elif N == 3:
        if s[0] == 1 and c[0] == 0:
            return -1
        elif s[1] == 2 and c[1] == 0:
            return -1
        else:
            return c[0] * 100 + c[1] * 10 + c[2]
    else:
        return -1
