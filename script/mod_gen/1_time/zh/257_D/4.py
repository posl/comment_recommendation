def getPower(s, x, y, xi, yi, pi):
    return pi * s >= abs(x - xi) + abs(y - yi)

if __name__ == '__main__':
    getPower()