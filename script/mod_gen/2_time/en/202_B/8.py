def rotate(s):
    s = s[::-1]
    return s.translate(str.maketrans("01689","01986"))
print(rotate(input()))

if __name__ == '__main__':
    rotate()