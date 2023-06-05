def get_key(s):
    a = [0 for i in range(26)]
    for i in s:
        a[ord(i) - ord('a')] += 1
    return tuple(a)
