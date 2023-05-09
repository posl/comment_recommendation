def median(a,b,c):
    if (a <= b and b <= c) or (c <= b and b <= a):
        return True
    else:
        return False
a,b,c = map(int, input().split())
