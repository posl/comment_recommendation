def countRL(s):
    r = 0
    l = 0
    for c in s:
        if c == 'R':
            r += 1
        else:
            l += 1
    return r, l

if __name__ == '__main__':
    countRL()