def convert(s, d):
    t = ''
    for c in s:
        t += str(d[c])
    return t

if __name__ == '__main__':
    convert()