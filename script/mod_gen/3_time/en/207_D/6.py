def rotate(x, y, theta):
    return (x * math.cos(theta) - y * math.sin(theta), x * math.sin(theta) + y * math.cos(theta))

if __name__ == '__main__':
    rotate()