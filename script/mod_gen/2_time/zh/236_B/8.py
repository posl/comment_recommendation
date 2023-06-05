def swap(s, a, b):
    a = a - 1
    b = b - 1
    s[a], s[b] = s[b], s[a]
    return s

if __name__ == '__main__':
    swap()