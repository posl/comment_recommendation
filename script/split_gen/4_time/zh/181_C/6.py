def isLine(point1, point2, point3):
    if (point2[0]-point1[0])*(point3[1]-point1[1]) == (point2[1]-point1[1])*(point3[0]-point1[0]):
        return True
    else:
        return False
