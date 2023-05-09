def getPoint(p1, p2, p3):
    if p1[0] == p2[0]:
        x = p3[0]
    elif p1[0] == p3[0]:
        x = p2[0]
    else:
        x = p1[0]
    if p1[1] == p2[1]:
        y = p3[1]
    elif p1[1] == p3[1]:
        y = p2[1]
    else:
        y = p1[1]
    return x, y

if __name__ == '__main__':
    getPoint()