def func(a,b):
    if a >= 13:
        return b
    elif 6 <= a <= 12:
        return b//2
    else:
        return 0
a,b = map(int,input().split())
print(func(a,b))
