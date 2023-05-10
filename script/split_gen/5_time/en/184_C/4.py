def ryuma(r1,c1,r2,c2):
    if r1==r2 and c1==c2:
        return 0
    elif r1+c1==r2+c2 or r1-c1==r2-c2 or abs(r1-r2)+abs(c1-c2)<=3:
        return 1
    elif (r1+c1)%2==(r2+c2)%2:
        return 2
    else:
        return 3
