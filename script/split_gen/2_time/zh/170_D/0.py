def find_nearest(x, p):
    #print("x: %d" % x)
    #print("p: %s" % p)
    if len(p) == 0:
        return x
    else:
        min = 100
        for i in p:
            if abs(x - i) < min:
                min = abs(x - i)
        return min + x
