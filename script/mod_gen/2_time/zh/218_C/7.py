def rotate90(m):
    return [list(x) for x in zip(*m[::-1])]

if __name__ == '__main__':
    rotate90()