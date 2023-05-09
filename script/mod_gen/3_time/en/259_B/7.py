def rotate(x,y,degree):
    import math
    degree = math.radians(degree)
    x = x * math.cos(degree) - y * math.sin(degree)
    y = x * math.sin(degree) + y * math.cos(degree)
    return x,y

if __name__ == '__main__':
    rotate()