def reverse(s, e, p):
    while s < e:
        p[s], p[e] = p[e], p[s]
        s += 1
        e -= 1
