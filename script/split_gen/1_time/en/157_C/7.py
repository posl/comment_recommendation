def check(n, s, c):
    for i in range(len(s)):
        if n[s[i] - 1] != c[i]:
            return False
    return True
