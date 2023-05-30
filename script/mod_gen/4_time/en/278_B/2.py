def confusing_time(h,m):
    while True:
        if m == 59:
            if h == 23:
                h = 0
                m = 0
            else:
                h += 1
                m = 0
        else:
            m += 1
        if h//10 == m%10 and h%10 == m//10:
            return h,m
h,m = map(int,input().split())
print(*confusing_time(h,m))
