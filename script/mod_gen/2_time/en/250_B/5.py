def get_tiles(n, a, b):
    tiles = []
    for i in range(n):
        for j in range(n):
            if i % 2 == 0:
                if j % 2 == 0:
                    tiles.append(['.'] * b)
                else:
                    tiles.append(['#'] * b)
            else:
                if j % 2 == 0:
                    tiles.append(['#'] * b)
                else:
                    tiles.append(['.'] * b)
    return tiles

if __name__ == '__main__':
    get_tiles()