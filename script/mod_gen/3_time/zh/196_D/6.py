def tiling(x, y):
    if x == 0 or y == 0:
        return 1
    elif x < 0 or y < 0:
        return 0
    else:
        return tiling(x-1, y) + tiling(x-2, y) + tiling(x, y-1) + tiling(x, y-2)

if __name__ == '__main__':
    tiling()