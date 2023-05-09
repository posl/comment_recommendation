def rotate(S):
    return [''.join(x) for x in zip(*S[::-1])]

if __name__ == '__main__':
    rotate()