def getDistance(a, b, h, m):
    if h >= 12:
        h = h - 12
    h = h + m/60
    if h >= 12:
        h = h - 12
    h = h * 30
    m = m * 6
    angle = abs(h - m)
    if angle > 180:
        angle = 360 - angle
    angle = angle * 3.1415926535897932384626433832795 / 180
    return (a ** 2 + b ** 2 - 2 * a * b * cos(angle)) ** 0.5

if __name__ == '__main__':
    getDistance()