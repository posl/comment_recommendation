def solve(x, y, z):
    if x > 0 and y < 0 and z < 0 and x + y < 0:
        return -1
    if x < 0 and y > 0 and z > 0 and x + y > 0:
        return -1
    return abs(x - z) + abs(y)
