def func(a,b):
    return round(b/a,4)
a,b = map(int,input().split())
print('{:.3f}'.format(func(a,b)))
