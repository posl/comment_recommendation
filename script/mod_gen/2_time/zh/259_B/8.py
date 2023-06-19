def rotate(a, b, d):
    import math
    theta = math.radians(d)
    a_ = a * math.cos(theta) - b * math.sin(theta)
    b_ = a * math.sin(theta) + b * math.cos(theta)
    return a_, b_

if __name__ == '__main__':
    rotate()