def reverse_string(s, l, r):
    s = list(s)
    for i in range(l-1, r):
        s[i] = s[r+l-2-i]
    return ''.join(s)
