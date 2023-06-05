def problems108_b(x1,y1,x2,y2):
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    return x3,y3,x4,y4

if __name__ == '__main__':
    problems108_b()