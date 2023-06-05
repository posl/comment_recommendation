def solve(s, t):
    for i in range(len(s)):
        if s[:i] + s[i+1:] == t:
            return i+1
    return len(s)+1
