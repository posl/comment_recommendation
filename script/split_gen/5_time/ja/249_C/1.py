def get_max_count(s, k):
    c = {}
    for i in range(len(s)):
        if s[i] in c:
            c[s[i]] += 1
        else:
            c[s[i]] = 1
    count = 0
    for v in c.values():
        if v == k:
            count += 1
    return count
