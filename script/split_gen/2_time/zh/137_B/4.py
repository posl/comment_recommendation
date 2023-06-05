def max(a,b):
    if a > b:
        return a
    else:
        return b
a,b = map(int,input().split())
print(max(a+b,a-b))
print(max(a+b,a*b))
