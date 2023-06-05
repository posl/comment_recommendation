def check(s, i):
    n = len(s)
    l = 0
    while i + l < n:
        if s[l] == s[i + l]:
            break
        l += 1
    return l
