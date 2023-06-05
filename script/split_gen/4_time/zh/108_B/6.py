def problems108_b(x1,y1,x2,y2):
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    print(x3, y3, x4, y4)
problems108_b(0, 0, 0, 1)
problems108_b(2, 3, 6, 6)
problems108_b(31, -41, -59, 26)
