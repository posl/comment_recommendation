def solve(s,t):
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    return count
