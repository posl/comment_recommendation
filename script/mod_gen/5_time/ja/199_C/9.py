def flip(s, a, b):
    return s[b:] + s[a:b] + s[:a]

if __name__ == '__main__':
    flip()