def median(a,b,c):
    if a < b:
        if b < c:
            return True
        else:
            return False
    else:
        if b > c:
            return True
        else:
            return False
a,b,c = map(int, input().split())
