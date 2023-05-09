def last_index(s, c):
    if c in s:
        return len(s) - s[::-1].index(c)
    else:
        return -1

if __name__ == '__main__':
    last_index()