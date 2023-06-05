def next_time(h,m):
    while True:
        if m<59:
            m+=1
        elif m==59:
            m=0
            if h<23:
                h+=1
            elif h==23:
                h=0
        if h//10==m%10 and h%10==m//10:
            return h,m
        else:
            continue

if __name__ == '__main__':
    next_time()