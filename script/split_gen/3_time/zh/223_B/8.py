def func(s):
    min_s = s
    max_s = s
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        min_s = min(min_s, s)
        max_s = max(max_s, s)
    return min_s, max_s
