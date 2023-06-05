def solve(h,w,a,b):
    if a == 0 and b == 0:
        return 1
    if a == 0:
        return 1
    if b == 0:
        return 1
    if a == 1 and b == 1:
        return 2
    if a == 1:
        return solve(h,w,a,b-1) + solve(h,w,a-1,b)
    if b == 1:
        return solve(h,w,a,b-1) + solve(h,w,a-1,b)
    return solve(h,w,a,b-1) + solve(h,w,a-1,b) + solve(h,w,a-2,b) + solve(h,w,a,b-2)
h,w,a,b = map(int,input().split())
print(solve(h,w,a,b))
