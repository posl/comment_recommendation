def solve(h,w,r,c):
    return 2*(r-1)*(c-1)+(h-r+1)*(c-1)+(w-c+1)*(r-1)+(h-r+1)*(w-c+1)
h,w=map(int,input().split())
r,c=map(int,input().split())
print(solve(h,w,r,c))
