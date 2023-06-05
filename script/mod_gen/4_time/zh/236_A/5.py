def swapchar(s,a,b):
    a = a - 1
    b = b - 1
    t = s[a]
    s[a] = s[b]
    s[b] = t
    return s

if __name__ == '__main__':
    swapchar()