def rotate90(l):
    # 90度回転
    return list(zip(*l[::-1]))

if __name__ == '__main__':
    rotate90()