def rotate_point(a,b,d):
    # a,b are the coordinates of the point
    # d is the degree of rotation
    import math
    d = math.radians(d)
    a_new = a*math.cos(d) - b*math.sin(d)
    b_new = a*math.sin(d) + b*math.cos(d)
    return a_new, b_new
a,b,d = map(float, input().split())
a_new, b_new = rotate_point(a,b,d)
print(a_new, b_new)
