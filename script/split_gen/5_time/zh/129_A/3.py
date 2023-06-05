def time_calc(p,q,r):
    return min(p+q,q+r,r+p)
p,q,r = map(int,input().split())
print(time_calc(p,q,r))
