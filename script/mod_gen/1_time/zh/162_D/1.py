def calc(s):
    r = 0
    g = 0
    b = 0
    for c in s:
        if c == 'R':
            r += 1
        elif c == 'G':
            g += 1
        else:
            b += 1
    return r, g, b

if __name__ == '__main__':
    calc()