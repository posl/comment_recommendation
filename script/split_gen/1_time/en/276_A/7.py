def last_index(s, c):
    return len(s) - s[::-1].index(c)
