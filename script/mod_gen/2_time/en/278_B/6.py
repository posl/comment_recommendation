def next_confusing_time(h,m):
    if h==23 and m==59:
        return 0,0
    if m==59:
        h+=1
        m=0
    else:
        m+=1
    while True:
        if h%10==m//10 and h//10==m%10:
            return h,m
        if h==23 and m==59:
            return 0,0
        if m==59:
            h+=1
            m=0
        else:
            m+=1
h,m=map(int,input().split())
print(*next_confusing_time(h,m))

if __name__ == '__main__':
    next_confusing_time()