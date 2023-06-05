def getNum(n):
    if n==1 or n==6 or n==9:
        return 1
    elif n==2 or n==7:
        return 2
    elif n==3 or n==8:
        return 3
    elif n==4:
        return 4
    elif n==5:
        return 5
    else:
        return 0

if __name__ == '__main__':
    getNum()