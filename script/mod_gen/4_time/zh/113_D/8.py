def f(h,w,k):
    if h==1:
        if k==1:
            return w
        else:
            return 0
    else:
        if k==1:
            return f(h-1,w,k)+f(h-1,w,k+1)
        elif k==w:
            return f(h-1,w,k-1)+f(h-1,w,k)
        else:
            return f(h-1,w,k-1)+f(h-1,w,k)+f(h-1,w,k+1)
h,w,k=map(int,input().split())
print(f(h,w,k)%1000000007)
