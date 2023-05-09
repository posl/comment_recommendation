def isTriangle(x1,y1,x2,y2,x3,y3):
    #print("isTriangle",x1,y1,x2,y2,x3,y3)
    if x1 == x2 and x2 == x3:
        return False
    if y1 == y2 and y2 == y3:
        return False
    if x1 == x2:
        return (y2-y1)*(x3-x2) != (y3-y2)*(x2-x1)
    if x2 == x3:
        return (y3-y2)*(x1-x3) != (y1-y3)*(x3-x2)
    if x1 == x3:
        return (y1-y3)*(x2-x1) != (y2-y1)*(x1-x3)
    return (y1-y3)*(x2-x1) != (y2-y1)*(x1-x3)

if __name__ == '__main__':
    isTriangle()