def swap(s,a,b):
    s = list(s)
    s[a-1],s[b-1] = s[b-1],s[a-1]
    return ''.join(s)
