def last_index(s, c):
    if c in s:
        return len(s) - s[::-1].index(c)
    else:
        return -1
