def swap(s, a, b):
    a = a - 1
    b = b - 1
    s = list(s)
    tmp = s[a]
    s[a] = s[b]
    s[b] = tmp
    return ''.join(s)

if __name__ == '__main__':
    swap()