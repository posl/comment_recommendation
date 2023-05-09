def rotate90(grid):
    return list(zip(*grid[::-1]))

if __name__ == '__main__':
    rotate90()