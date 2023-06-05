def amidakuji(h,w,k):
    if w==1:
        if h==1:
            return 1
        elif h==2:
            if k==1:
                return 1
            elif k==2:
                return 2
            else:
                return 0
        else:
            if k==1:
                return 1
            elif k==2:
                return 2
            elif k==3:
                return 4
            else:
                return 0
    else:
        if h==1:
            if k==1:
                return 1
            else:
                return 0
        elif h==2:
            if k==1:
                return 1
            elif k==2:
                return 2
            else:
                return 0
        else:
            if k==1:
                return 1
            elif k==2:
                return 2
            elif k==3:
                return 4
            elif k==4:
                return 8
            elif k==5:
                return 16
            else:
                return 0
h,w,k=map(int,input().split())
print(amidakuji(h,w,k))
