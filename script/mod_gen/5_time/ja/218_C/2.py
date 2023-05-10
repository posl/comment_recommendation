def rotate_90(ary):
    return list(map(list, zip(*ary[::-1])))

if __name__ == '__main__':
    rotate_90()