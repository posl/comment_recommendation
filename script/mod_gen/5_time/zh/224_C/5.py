def getArea(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs(x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2)
    return area

if __name__ == '__main__':
    getArea()