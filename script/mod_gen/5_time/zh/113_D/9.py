def amidakuji(h,w,k):
    if w == 1:
        return 1
    elif k == 1:
        return amidakuji(h,w-1,1) + amidakuji(h,w-1,2)
    elif k == w:
        return amidakuji(h,w-1,w-1) + amidakuji(h,w-1,w)
    else:
        return amidakuji(h,w-1,k-1) + amidakuji(h,w-1,k) + amidakuji(h,w-1,k+1)

if __name__ == '__main__':
    amidakuji()