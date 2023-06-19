def solve(n, t):
    if n == 1:
        return t[0]
    elif n == 2:
        return max(t[0], t[1])
    else:
        return max(t[0] + solve(n-1, t[1:]), t[-1] + solve(n-1, t[:-1]))
