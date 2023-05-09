def rotate90(S):
    return [list(reversed(s)) for s in zip(*S)]

if __name__ == '__main__':
    rotate90()