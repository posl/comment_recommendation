def rotate(x,y,deg):
    rad = math.radians(deg)
    x2 = x * math.cos(rad) - y * math.sin(rad)
    y2 = x * math.sin(rad) + y * math.cos(rad)
    return x2,y2

if __name__ == '__main__':
    rotate()