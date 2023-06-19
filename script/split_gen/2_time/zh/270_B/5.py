def solve(x, y, z):
    if y > 0 and z > 0:
        return -1
    if y < 0 and z < 0:
        return -1
    if y > 0 and y > z:
        return -1
    if y < 0 and y < z:
        return -1
    return abs(x - y)
