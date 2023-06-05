def lexicographical_order(s):
    s = list(s)
    s.sort()
    return ''.join(s)
