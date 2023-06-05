def get_min_max(s):
    min = s
    max = s
    for i in range(0, len(s)):
        s = s[1:] + s[0]
        if s < min:
            min = s
        elif s > max:
            max = s
    return min, max
