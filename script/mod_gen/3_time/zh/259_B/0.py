def rotate(a, b, d):
    import math
    d = math.radians(d)
    a_ = a*math.cos(d)-b*math.sin(d)
    b_ = a*math.sin(d)+b*math.cos(d)
    return a_, b_

if __name__ == '__main__':
    rotate()