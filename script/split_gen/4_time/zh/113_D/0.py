def func(h,w,k):
    #h,w,k=map(int,input().split())
    #h,w,k=1,3,2
    #h,w,k=1,3,1
    #h,w,k=2,3,3
    #h,w,k=2,3,1
    #h,w,k=7,1,1
    #h,w,k=15,8,5
    if k==1:
        if h==1:
            return 1
        else:
            return 2**(h-2)
    elif k==w:
        if h==1:
            return 1
        else:
            return 2**(h-2)
    else:
        if h==1:
            return 1
        else:
            return 2**(h-3)
    #print(h,w,k)
    #print(2**(h-2))
    #print(2**(h-3))
    #print(2**(h-2)+2**(h-3))
    #print(2**(h-2)+2**(h-3)-2)
    #print(2**(h-2)+2**(h-3)-2-2**(h-3))
    #print(2**(h-2)+2**(h-3)-2-2**(h-3)-2**(h-3))
    #print(2**(h-2)+2**(h-3)-2-2**(h-3)-2**(h-3)-2**(h-3))
    #print(2**(h-2)+2**(h-3)-2-2**(h-3)-2**(h-3)-2**(h-3)-2**(h-3))
    #print(2**(h-2)+2**(h-3)-2-2**(h-3)-2**(h-3)-2**(h-3)-2**(h-3)-2**(h-3))
