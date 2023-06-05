def count(s):
    t = [0]*26
    for c in s:
        t[ord(c)-ord('a')] = 1
    return t.count(1)
