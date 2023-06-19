def search(x, y, z):
    if x == 0:
        return True
    if y == 0:
        return False
    if x < z[0][0]:
        return False
    if x // z[0][0] <= z[0][1]:
        return search(x % z[0][0], y - 1, z[1:])
    else:
        return search(x - z[0][0] * z[0][1], y - 1, z[1:])

if __name__ == '__main__':
    search()