def f(h,w,a,b):
    if h==0 and w==0:
        return 1
    if h<0 or w<0:
        return 0
    if h<w:
        h,w=w,h
    if h==w:
        return f(h-1,w-1,a,b)
    return f(h-1,w,a,b)+f(h-2,w,a,b)+f(h-1,w-1,a,b)+f(h-2,w-2,a,b)
h,w,a,b=map(int,input().split())
print(f(h,w,a,b))
