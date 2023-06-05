def reverse_string(s, l, r):
    s = list(s)
    for i in range(l-1, (l+r)/2):
        tmp = s[i]
        s[i] = s[r-i+l-1]
        s[r-i+l-1] = tmp
    return ''.join(s)
