def solve(s, t):
    for i in range(len(t)):
        if t[:i] + t[i + 1:] == s:
            return i + 1
    return len(t) + 1
