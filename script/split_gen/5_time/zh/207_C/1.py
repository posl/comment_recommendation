def intersection(a,b):
    if a[0]==1:
        if b[0]==1:
            if a[1]<=b[2]:
                return True
            else:
                return False
        elif b[0]==2:
            if a[1]<b[2]:
                return True
            else:
                return False
        elif b[0]==3:
            if a[1]<b[2]:
                return True
            else:
                return False
        elif b[0]==4:
            if a[1]<b[2]:
                return True
            else:
                return False
    elif a[0]==2:
        if b[0]==1:
            if a[2]>b[1]:
                return True
            else:
                return False
        elif b[0]==2:
            if a[2]>b[1]:
                return True
            else:
                return False
        elif b[0]==3:
            if a[2]>b[1]:
                return True
            else:
                return False
        elif b[0]==4:
            if a[2]>b[1]:
                return True
            else:
                return False
    elif a[0]==3:
        if b[0]==1:
            if a[2]>=b[1]:
                return True
            else:
                return False
        elif b[0]==2:
            if a[2]>b[1]:
                return True
            else:
                return False
        elif b[0]==3:
            if a[2]>b[1]:
                return True
            else:
                return False
        elif b[0]==4:
            if a[2]>b[1]:
                return True
            else:
                return False
    elif a[0]==4:
        if b[0]==1:
            if a[2]>b[1]:
                return True
            else:
                return False
        elif b[0]==2:
            if a[2]>b[1]:
                return True
            else:
                return False
        elif b[0]==3:
            if a[2]>b[1]:
                return True
            else:
                return False
        elif b[0]==4:
            if a[2]>b[1]:
                return True
            else:
                return False
