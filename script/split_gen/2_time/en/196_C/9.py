def count(n):
    s = str(n)
    l = len(s)
    if l % 2 == 1:
        return 0
    else:
        l2 = l // 2
        s1 = s[:l2]
        s2 = s[l2:]
        if s1 == s2:
            return 1
        else:
            return 0
