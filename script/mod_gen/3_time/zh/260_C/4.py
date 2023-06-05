def change(n,x,y):
    if n==1:
        return 0
    if n==2:
        return 1
    if n==3:
        return x+1
    if n==4:
        return x+y+1
    return change(n-1,x,y)+change(n-2,x,y)+change(n-3,x,y)+change(n-4,x,y)+x+y

if __name__ == '__main__':
    change()