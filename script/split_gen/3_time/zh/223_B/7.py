def min_max(s):
    s = list(s)
    min_s = s[:]
    max_s = s[:]
    for i in range(len(s)):
        s.append(s.pop(0))
        if s < min_s:
            min_s = s[:]
        elif s > max_s:
            max_s = s[:]
    return ''.join(min_s), ''.join(max_s)
