def reverseString(s, start, end):
    if start < 0 or end >= len(s):
        return -1
    for i in range((end - start + 1) // 2):
        s[start + i], s[end - i] = s[end - i], s[start + i]
    return s
