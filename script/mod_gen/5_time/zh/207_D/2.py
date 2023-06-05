def rotate(p, theta):
    return (p[0]*math.cos(theta) - p[1]*math.sin(theta), p[0]*math.sin(theta) + p[1]*math.cos(theta))

if __name__ == '__main__':
    rotate()