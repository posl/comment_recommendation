def f(h,w,a,b):
    if w==0:
        return 1
    if h*w%2==0 and a>0:
        return f(h,w-1,a-1,b)+f(h,w-2,a-1,b)
    if h*w%2==0 and b>0:
        return f(h,w-1,a,b-1)+f(h,w-1,a,b-1)
    return f(h,w-1,a,b)
h,w,a,b=map(int,input().split())
print(f(h,w,a,b))
