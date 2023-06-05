def solve(x,y,z):
    if (y-x)*(z-y) > 0:
        return abs(y-x)
    else:
        return -1
