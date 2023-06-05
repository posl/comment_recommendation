def is_convex(a,b,c,d):
    def is_left(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    def is_same_side(a,b,c,d):
        return is_left(a,b,c)*is_left(a,b,d)>=0
    return is_same_side(a,b,c,d) and is_same_side(b,c,a,d) and is_same_side(c,d,a,b)
