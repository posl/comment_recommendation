def flip(s, a, b):
    return s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]

if __name__ == '__main__':
    flip()