def confusing_time(h,m):
    n = 60*h + m
    while True:
        n = (n+1)%(24*60)
        t = n//60
        u = n%60
        if (t//10==u%10) and (t%10==u//10):
            return t,u
h,m = map(int, input().split())
t,u = confusing_time(h,m)
print(t,u)
