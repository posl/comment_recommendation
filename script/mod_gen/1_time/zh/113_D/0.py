def amidakuji(h,w,k):
    if h==1:
        if k==1:
            return 1
        else:
            return 2
    else:
        if k==1:
            return 1
        elif k==w:
            return 1
        else:
            return amidakuji(h-1,w-1,k-1)+amidakuji(h-1,w-1,k)

if __name__ == '__main__':
    amidakuji()