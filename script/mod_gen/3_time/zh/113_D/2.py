def amidakuji(h,w,k):
    if k == 1 or k == w:
        return 1
    elif k == 2:
        return w*(w-1)
    else:
        return w*(w-1)*(w-2)

if __name__ == '__main__':
    amidakuji()