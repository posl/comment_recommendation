def max(a,b):
    if a+b>a-b:
        if a+b>a*b:
            return a+b
        else:
            return a*b
    else:
        if a-b>a*b:
            return a-b
        else:
            return a*b
a,b=map(int,input().split())
print(max(a,b))
