def rotate90(S):
    return list(map(list,zip(*S[::-1])))

if __name__ == '__main__':
    rotate90()