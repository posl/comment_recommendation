def func(h,w,k):
    if w == 1:
        if k == 1:
            return 1
        else:
            return 0
    else:
        if k == 1:
            return func(h,w-1,1) + func(h,w-1,2)
        elif k == w:
            return func(h,w-1,w-1) + func(h,w-1,w)
        else:
            return func(h,w-1,k-1) + func(h,w-1,k) + func(h,w-1,k+1)

if __name__ == '__main__':
    func()