def knight(x,y):
    if x==0 and y==0:
        return 1
    elif x<0 or y<0:
        return 0
    else:
        return (knight(x-2,y-1)+knight(x-1,y-2))%1000000007

if __name__ == '__main__':
    knight()