def rotate_90(l):
    return list(map(list, zip(*l[::-1])))

if __name__ == '__main__':
    rotate_90()