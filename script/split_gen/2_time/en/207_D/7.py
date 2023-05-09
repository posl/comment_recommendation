def rotate(x, y, p):
    rad = math.radians(p)
    return (x*math.cos(rad)-y*math.sin(rad), x*math.sin(rad)+y*math.cos(rad))
