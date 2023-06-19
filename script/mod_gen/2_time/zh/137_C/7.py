def count(s):
    # s is a string
    # return a dictionary
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

if __name__ == '__main__':
    count()