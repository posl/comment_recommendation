def solve(x,y,z):
    if (x>0 and y>0 and z>0) or (x<0 and y<0 and z<0):
        return -1
    elif x>0 and y>0 and z<0:
        return abs(x-y)
    elif x>0 and y<0 and z>0:
        return x+y
    elif x<0 and y>0 and z>0:
        return y+z
    elif x<0 and y<0 and z>0:
        return abs(x-z)
    elif x<0 and y>0 and z<0:
        return abs(x-y)+abs(y-z)
    elif x>0 and y<0 and z<0:
        return abs(x-z)
    else:
        return abs(x-y)+abs(y-z)
