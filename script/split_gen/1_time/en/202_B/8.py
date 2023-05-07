def rotate(s):
    return s[::-1].translate(str.maketrans('01689', '01986'))
