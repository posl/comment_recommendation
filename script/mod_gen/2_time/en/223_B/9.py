def rotate_left(s, n):
    return s[n:] + s[:n]

if __name__ == '__main__':
    rotate_left()