def mid(a,b,c):
    if a <= b <= c or c <= b <= a:
        return True
    else:
        return False
a,b,c = map(int,input().split())
