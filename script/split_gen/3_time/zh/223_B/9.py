def min_max(s):
    s = s+s
    min_s = s
    max_s = s
    for i in range(len(s)):
        if s[i:] + s[:i] < min_s:
            min_s = s[i:] + s[:i]
        if s[i:] + s[:i] > max_s:
            max_s = s[i:] + s[:i]
    return min_s[:len(s)//2], max_s[:len(s)//2]
