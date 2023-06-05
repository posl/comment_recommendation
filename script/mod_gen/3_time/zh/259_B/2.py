def rotate_point(a,b,d):
    import math
    d = math.radians(d)
    a_new = a*math.cos(d) - b*math.sin(d)
    b_new = a*math.sin(d) + b*math.cos(d)
    return a_new,b_new

if __name__ == '__main__':
    rotate_point()