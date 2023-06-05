def rotate(x,y,d):
    import math
    d = math.radians(d)
    a = x*math.cos(d) - y*math.sin(d)
    b = x*math.sin(d) + y*math.cos(d)
    return a,b

if __name__ == '__main__':
    rotate()