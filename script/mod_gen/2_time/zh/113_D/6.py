def amidakuji(h,w,k):
    #print(h,w,k)
    if k == 1:
        return 2**(w-1)
    elif k == w:
        return 2**(w-1)
    else:
        return 2**(w-2)

if __name__ == '__main__':
    amidakuji()