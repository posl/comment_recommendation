def getdist(a,b,h,m):
    hangle = (h + m/60)*30
    mangle = m * 6
    hangle = hangle * math.pi / 180
    mangle = mangle * math.pi / 180
    return math.sqrt(a*a + b*b - 2*a*b*math.cos(abs(hangle-mangle)))

if __name__ == '__main__':
    getdist()