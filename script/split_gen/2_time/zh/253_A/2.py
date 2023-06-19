def median(a,b,c):
    if b >= a >= c or c >= a >= b:
        return "是"
    else:
        return "没有"
a,b,c = map(int,input().split())
print(median(a,b,c))
