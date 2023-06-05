def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a,b = map(int,input().split())
print(max(a+b,a-b,a*b))
