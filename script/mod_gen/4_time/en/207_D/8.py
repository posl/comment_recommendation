def rotate(x,y,deg):
    rad = deg/180*math.pi
    return x*math.cos(rad)-y*math.sin(rad), x*math.sin(rad)+y*math.cos(rad)

if __name__ == '__main__':
    rotate()