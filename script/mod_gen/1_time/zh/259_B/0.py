def rotate_point(x,y,d):
    import math
    rad = math.radians(d)
    new_x = x*math.cos(rad) - y*math.sin(rad)
    new_y = x*math.sin(rad) + y*math.cos(rad)
    return new_x,new_y

if __name__ == '__main__':
    rotate_point()