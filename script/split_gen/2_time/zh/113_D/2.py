def amidakuji(h,w,k):
    if h == 1:
        if k == 1:
            return 1
        elif k == w:
            return 2
        else:
            return 0
    else:
        if k == 1:
            return amidakuji(h-1,w,k)
        elif k == w:
            return amidakuji(h-1,w-1,k-1)
        else:
            return amidakuji(h-1,w,k) + amidakuji(h-1,w-1,k-1)
h,w,k = map(int,input().split())
print(amidakuji(h,w,k)%1000000007)
