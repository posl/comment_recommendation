def getTile(n,a,b):
    tile = []
    for i in range(n):
        line = ""
        for j in range(n):
            if (i+j)%2 == 0:
                line += "."*b
            else:
                line += "#"*b
        tile.append(line)
    return tile

if __name__ == '__main__':
    getTile()