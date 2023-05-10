def median(a,b,c):
    if (b>a and b<c) or (b<a and b>c):
        return True
    else:
        return False
a,b,c = map(int,input().split())
