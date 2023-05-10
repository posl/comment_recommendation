def solve(s, t):
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            return True
    return False
