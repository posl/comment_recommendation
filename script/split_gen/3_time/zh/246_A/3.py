def solution(x1,y1,x2,y2,x3,y3):
    x4 = x3 - (y3-y2)
    y4 = y3 + (x3-x2)
    return x4, y4
