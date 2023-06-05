def solve(x,y,z):
    if y > z:
        return -1
    else:
        return abs(x-y)+abs(y-z)
