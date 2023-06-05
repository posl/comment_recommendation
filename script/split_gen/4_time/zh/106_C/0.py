def func(s, k):
    if k < len(s):
        return s[k-1]
    else:
        return func(s, k-len(s))
