def rotate_90(s):
    return list(zip(*s[::-1]))

if __name__ == '__main__':
    rotate_90()