def isPoor(a,b,c):
    return (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a)
