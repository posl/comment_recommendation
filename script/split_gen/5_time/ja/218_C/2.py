def rotate_90(ary):
    return list(map(list, zip(*ary[::-1])))
