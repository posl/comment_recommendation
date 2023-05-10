def is_median(a,b,c):
    if a <= b <= c or c <= b <= a:
        return True
    return False
a,b,c = map(int,input().split())
