def checkbuy(n,x,alist):
    for i in range(0,n):
        if i%2 == 0:
            x = x - alist[i]
        else:
            x = x - alist[i] + 1
    if x >= 0:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    checkbuy()