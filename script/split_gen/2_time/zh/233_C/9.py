def reverse(s, l, r):
    s = list(s)
    s[l-1:r] = reversed(s[l-1:r])
    return "".join(s)
