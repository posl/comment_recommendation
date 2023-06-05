def solve(s,t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return i+1
    return len(s)+1
