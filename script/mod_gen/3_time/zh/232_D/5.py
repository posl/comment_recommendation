def isWall(x, y):
    if x >= 0 and x < H and y >= 0 and y < W:
        if maze[x][y] == '#':
            return True
    return False

if __name__ == '__main__':
    isWall()