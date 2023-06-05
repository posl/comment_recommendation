def count(s):
    s = list(s)
    s.sort()
    s = ''.join(s)
    return s

if __name__ == '__main__':
    count()