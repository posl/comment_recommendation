def f(h,w,a,b):
    if h == 1 and w == 1:
        return 1
    if h == 1:
        return f(1,w-1,b,a)
    if w == 1:
        return f(h-1,1,a,b)
    if h == 2 and w == 2:
        return 4
    if h == 2:
        return f(2,w-1,b,a) + f(2,w-2,b,a)
    if w == 2:
        return f(h-1,2,a,b) + f(h-2,2,a,b)
    return f(h-1,w,a,b) + f(h-2,w,a,b) + f(h,w-1,a,b) + f(h,w-2,a,b)
h,w,a,b = map(int,input().split())
print(f(h,w,a,b))
