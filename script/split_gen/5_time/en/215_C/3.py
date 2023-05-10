def permute(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return s
    else:
        l = []
        for i in range(len(s)):
            x = s[i]
            xs = s[:i] + s[i+1:]
            for p in permute(xs):
                l.append(x + p)
        return l
