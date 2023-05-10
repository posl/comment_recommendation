def rotate_point(a, b, d):
    import math
    rad = math.radians(d)
    a_new = a*math.cos(rad) - b*math.sin(rad)
    b_new = a*math.sin(rad) + b*math.cos(rad)
    return a_new, b_new

if __name__ == '__main__':
    rotate_point()