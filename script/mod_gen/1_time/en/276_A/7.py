def last_index(s, c):
    return len(s) - s[::-1].index(c)

if __name__ == '__main__':
    last_index()