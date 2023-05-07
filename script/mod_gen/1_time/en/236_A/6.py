def swap(s, a, b):
    a-=1
    b-=1
    s[a], s[b] = s[b], s[a]
    return ''.join(s)

if __name__ == '__main__':
    swap()