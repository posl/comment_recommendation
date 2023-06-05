def median(a,b,c):
    if b>=a and b<=c:
        return True
    elif b<=a and b>=c:
        return True
    else:
        return False
a,b,c = map(int,input().split())
