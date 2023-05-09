def SGS(n):
    if n<357:
        return 0
    elif n<375:
        return 1
    elif n<537:
        return 2
    elif n<573:
        return 3
    elif n<735:
        return 4
    elif n<753:
        return 5
    elif n<1000:
        return 6
    else:
        n=str(n)
        l=len(n)
        s=0
        for i in range(3,l-2):
            s+=C(i-1,2)*C(l-i-1,2)*C(3,1)*C(3,1)*C(3,1)
        for i in range(3,l-1):
            s+=C(i-1,2)*C(l-i-1,1)*C(3,1)*C(3,1)
        for i in range(3,l):
            s+=C(i-1,1)*C(3,1)*C(3,1)
        s+=C(3,1)*C(3,1)
        return s

if __name__ == '__main__':
    SGS()