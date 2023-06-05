def f(h,w,a,b):
    if h<2 or w<2:
        return 1
    if a==0 and b==0:
        return 1
    if (h,w,a,b) in memo:
        return memo[(h,w,a,b)]
    if a>0:
        ans=f(h-2,w,a-1,b)+f(h-1,w-1,a-1,b)+f(h-2,w,a-1,b)+f(h-1,w-1,a-1,b)
    else:
        ans=f(h-1,w-1,a,b-1)+f(h-1,w-1,a,b-1)
    memo[(h,w,a,b)]=ans
    return ans
memo={}
h,w,a,b=map(int,input().split())
print(f(h,w,a,b))
