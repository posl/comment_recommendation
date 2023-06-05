def reverse_string(s, l, r):
    s = list(s)
    for i in range(l-1, r):
        s[i] = s[r-1+l-i-1]
    return ''.join(s)
