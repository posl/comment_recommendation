def paint_tile(tile, a, b):
    for i in range(a):
        for j in range(b):
            if i % 2 == 0:
                tile[i][j] = "."
            else:
                tile[i][j] = "#"
    return tile

if __name__ == '__main__':
    paint_tile()