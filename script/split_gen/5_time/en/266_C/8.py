def check_convex_quadrilateral(a,b,c,d):
    if (a[0]-b[0])*(a[1]-d[1]) == (a[0]-d[0])*(a[1]-b[1]) and (b[0]-c[0])*(b[1]-a[1]) == (b[0]-a[0])*(b[1]-c[1]) and (c[0]-d[0])*(c[1]-b[1]) == (c[0]-b[0])*(c[1]-d[1]) and (d[0]-a[0])*(d[1]-c[1]) == (d[0]-c[0])*(d[1]-a[1]):
        return False
    else:
        return True
