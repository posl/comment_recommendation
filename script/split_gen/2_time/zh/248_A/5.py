def find_missing_number(s):
    s = list(s)
    s = map(int, s)
    s.sort()
    for i in range(0, len(s)):
        if s[i] != i:
            return i
    return 9
