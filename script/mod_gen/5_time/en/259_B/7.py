def rotate(a,b,d):
    from math import sin, cos, radians
    rad = radians(d)
    a1 = a*cos(rad) - b*sin(rad)
    b1 = a*sin(rad) + b*cos(rad)
    return a1,b1

if __name__ == '__main__':
    rotate()